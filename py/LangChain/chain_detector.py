import time
import tools
from difflib import get_close_matches
template_context= """
You are an inconsistency detector for privacy APIs. I will provide you the following information:

1. Requirements: The mandatory requirements should be met
2. Context: Events that occurred before this API invocation.

Your Task: Detect inconsistencies between the context and requirements that could lead to security or privacy issues.

Instructions:
1. Report absence or inconsistencies that contradict the requirements and can result in security or privacy vulnerabilities; 
2. Avoid Over-Speculation: Do not infer issues beyond the provided information. Only report inconsistencies that are evident and substantiated by the data.

Output Format:
1. If you do no found any inconsistency, output "no inconsistency found"
2. If you find inconsistencies/conflicts that can lead to security or privacy issues with high confidence, please output:
[
    {{
        "inconsistency": "", // Overview of the inconsistency.
        "description": "", // Explain why this is an inconsistency.
        "Security/Privacy Issue": "", // What security or privacy issue that this inconsistency can cause
    }}
]

Example:
**Example Start**
Obligatory requirements:
User does not opt out of interest-based advertising.

context:

IP: Euro, Paris
Age: 14 Years old
APP target user: Everyone

1. Display: Displays a dialog requesting the user’s authorization to opt in data sharing and interest-based advertising.
2. Click "Decline" in a dialog requesting the user’s authorization to opt in data sharing interest-based advertising.


Output:
[
    {{
        "inconsistency": "Set do not sell to False but user has opt out data sharing"
        "description": "The context indicates that the user clicked the Decline button in the dialog requesting permission for interest-based advertising, indicating that the user has opted out. This action contradicts the constraints.",
        "Security/Privacy Issue": "The API’s parameter settings are inconsistent with the user’s choices, potentially resulting in unexpected even illegal interest-based advertising and data sharing."
    }}
]

**Example End**

% Obligatory requirements
{requirements}

% context
{context}

"""


template_expectation = """
You are an inconsistency detector for privacy APIs. I will provide you the following information:

1. Expectations: The forbidden event/behaviour that should not occur
2. Subsequent Events: Events that occurred after this API invocation.

Your Task: Detect inconsistencies between the Subsequent Events and Expectations that could lead to security or privacy issues.

Instructions:
1. Report inconsistencies that contradict the Expectations and can result in security or privacy vulnerabilities; 
2. Avoid Over-Speculation: Do not infer issues beyond the provided information. Only report inconsistencies that are evident and substantiated by the data.

Output Format:
1. If you do no found any inconsistency, output "no inconsistency found"
2. If you find inconsistencies/conflicts that can lead to security or privacy issues with high confidence, please output:
[
    {{
        "inconsistency": "", // Overview of the inconsistency.
        "description": "", // Explain why this is an inconsistency.
        "Security/Privacy Issue": "" // What security or privacy issue that this inconsistency can cause.
    }}
]

Examples:
**Example1 Start**
Privacy API:
call 'setDoNotSell' of class 'com.applovin.sdk.AppLovinPrivacySettings' with arguments 'true', return undefined; Expectations: The user will not receive personalized advertisements. The user can receive contextual ads.

subsequent events:
1. Call method build of Class com.google.android.gms.ads.RequestConfiguration$Builder; with parameters []; return com.google.android.gms.ads.RequestConfiguration@f8
2. Call method setRequestConfiguration of Class com.google.android.gms.ads.MobileAds; with parameters ['com.google.android.gms.ads.RequestConfiguration@f864e3c']; return undefined
3. Display: Displays an advertisement labeled “You may be interested in.”


Output:
[
    {{
        "inconsistency": "Unexpected behavior happened"
        "description": "Personalized ads are not permitted; however, the label 'You may be interested in.' implies that the ad is likely personalized.",
        "Security/Privacy Issue": "unauthorized data usage and advertising practices"
    }}
]

**Example End**

**Example2 Start**
Privacy API:
call 'setDoNotSell' of class 'com.applovin.sdk.AppLovinPrivacySettings' with arguments 'false', return undefined; Expectations: The user can receive personalized advertisements.

subsequent events:
1. Call method build of Class com.google.android.gms.ads.RequestConfiguration$Builder; with parameters []; return com.google.android.gms.ads.RequestConfiguration@f8
2. Call method setRequestConfiguration of Class com.google.android.gms.ads.MobileAds; with parameters ['com.google.android.gms.ads.RequestConfiguration@f864e3c']; return undefined


Output:
no inconsistency found. // Although no personalized advertisements were displayed, there is no inconsistency. This is because "The user can receive personalized advertisements" is neither forbidden nor obligatory—it is simply optional and permissive. Therefore, there are no constraints in the expectations, and detection is not necessary.

**Example2 End**




% expectations
{expectations}

% Subsequent Events
{subsequent_events}

"""

forbidden_exp_prompt = """
You are tasked with extracting forbidden behaviors from a given input sentence that describes expectations. Please use user's (not developers') perspective. Forbidden behaviors are actions or conditions explicitly stated as not allowed or prohibited. Ignore any optional, allowable, or permissive expectations that typically use keywords like "can," "allow," or "permitted."
 
**Input**:
A string describing expectations.

**Output**:
1. If prohibited behaviors or events are identified in the expectations, output a list of forbidden behaviors explicitly mentioned in the input.
2. If no forbidden behaviors are found, return "not found".

% expectations
{expectations}

"""

forbidden_exp_prompt_v2 = """
You are tasked with extracting forbidden behaviors from a given input sentence that describes expectations. Forbidden behaviors refer to actions or conditions explicitly stated as not allowed or prohibited. Ignore any optional, permissible, or allowable expectations typically indicated by keywords such as "can," "allow," or "permitted."

Instructions:
1. Extract forbidden behaviors from the input text and output them in the format: "Forbid ..."
2. Include the pattern used for extraction alongside the forbidden behavior.
3. If no forbidden behaviors are found, return "Not found".

Patterns for Forbidden Behaviors:
Pattern 1 - be/will/can/do not: User's personal information will not be used for advertising -> Forbid user's personal information being used for advertising.
Pattern 2 - no...will/no longer: Adjust will no longer receive data from this user/device -> Forbid Adjust receiving data from this user/device
Pattern 3 - disable/disallow/prevent/prohibit/reject/deny/avoid/opt-out: Disables third-party sharing -> Forbid third-party sharing
Pattern 4 - stop/cease/pause/turn off: Stops Adjust from sharing user data with third parties -> Forbid Adjust from sharing user data with third parties 
Pattern 5 - only : Only contextual ads will be shown to the user -> Forbid non-contextual ads being shown to the user.
Pattern 6 - all: All ads served will be non-personalized -> Forbid ads served being personalized.
Pattern 7 - restrict: Restrict the sale of personal information under CCPA -> Forbid the sale of personal information under CCPA.

**Input**:
A string describing expectations.

**Output**:
1. If prohibited behaviors are identified, output a list of forbidden behaviors explicitly mentioned, formatted as: "Forbidden event (Pattern X)"
Example: ["Forbid third-party sharing (Pattern 3)", "Forbid ads served being personalized (Pattern 6)"]
2. If no forbidden behaviors are found, output "Not found".

% expectations
{expectations}

"""

obligatory_con_prompt = """
You are tasked with extracting obligatory requirements from a given input sentence that describes conditions.Please use user's (not developers') perspective. Obligatory conditions are actions or conditions explicitly stated as mandatory requirements that must be fulfilled. Ignore any optional, allowable, or permissive conditions.

**Input**:
A string describing conditions.

**Output**:
1. If obligatory conditions are identified in the conditions, out put a list of obligatory conditions mentioned in the input.
2. If no obligatory conditions are found, return "not found"

% conditions
{conditions}

"""

from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import json
from langchain.chains import LLMChain
from langchain import OpenAI
import os
from tools import isPricacyAPI
from langchain.agents import load_tools
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=os.getenv('OPENAI_API_KEY'))

prompt_context = PromptTemplate(input_variables=["trace", "context"],template=template_context)
prompt_exp = PromptTemplate(input_variables=["trace", "subsequent_events"],template=template_expectation)
prompt_forbid = PromptTemplate(input_variables=["expectations"],template=forbidden_exp_prompt_v2)
prompt_obl = PromptTemplate(input_variables=["conditions"],template=obligatory_con_prompt)
def get_obligatory_constraint(conditions, apk):
    try:
        chain = LLMChain(llm=llm, prompt=prompt_obl)
        result = chain.run(conditions=conditions)
        print(result)
        with open(f"res/constrains/{apk}.log", "a") as file:
            file.write(
                f"conditions:\n{conditions}\nobligatory:{result}\n--------------------------------------------------------------------------------------\n\n")
        return result
    except Exception as e:
        print(f"error {e}")
        return ""
def get_forbidden_constraint(expectations, apk):
    try:
        chain = LLMChain(llm=llm, prompt=prompt_forbid)
        result = chain.run(expectations=expectations)
        print(result)
        with open(f"res/constrains/{apk}.log", "a") as file:
            file.write(
                f"expectations:\n{expectations}\nobligatory:{result}\n--------------------------------------------------------------------------------------\n\n")
        return result
    except Exception as e:
        print(f"error {e}")
        return ""

def chain_detector(apk):
    if not os.path.exists(f"res/context/{apk}.json"):
        return None

    with open(f'res/context/{apk}.json', 'r') as f:
        context_raw = f.read()

    with open(f'res/profile/{apk}.log', 'r') as f:
        profile_data = f.read()

    context_raw = context_raw.replace("][", ",")
    context_js = json.loads(context_raw)
    contexts = sorted(context_js, key=lambda x: x['timestamp'])

    for context in contexts:
        if not "is_privacy_api" in context.keys() or not context["is_privacy_api"]:
            continue
        condition_text = ""
        effect_text = ""
        effect_list = []
        condition_list = []
        index_con = 1
        index_exp = 1
        for context2 in contexts:
            des = ""
            if "description" in context2.keys() and context2["description"]:
                des = f"{context2['description']};"
            if context2["timestamp"] < context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in condition_list:
                    condition_text += str(index_con) + ". " + des + context2["context"] + "\n"
                    condition_list.append(context2["context"])
                    index_con += 1
                # if "premise" in context.keys() and context["premise"] and context["premise"] not in premise_list:
                #     premise_text += context["premise"] + "\n"
                #     premise_list.append(context["premise"])
            elif context2["timestamp"] > context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in effect_list:
                    effect_text += str(index_exp) + ". " + des +context2["context"] + "\n"
                    effect_list.append(context2["context"])
                    index_exp += 1
        if context['context'] and len(context['context'].strip()) > 0:

            req = get_obligatory_constraint(context['context'], apk)
            if 'not found' not in req.lower():
                try:
                    chain = LLMChain(llm=llm, prompt=prompt_context)
                    condition_text = f"{profile_data}\n\n {condition_text}"
                    result = chain.run(requirements=req, context=condition_text)
                    with open(f"res/detection/context/{apk}.log", "a") as file:
                        file.write(
                            f"requirement:\n{req}\nContext:\n{condition_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")

                except Exception as e:
                    print(f"error {e}")
                time.sleep(2)
            else:
                with open(f"res/detection/context/{apk}.log", "a") as file:
                    file.write(
                        f"requirement:\n{req}\nConstraint Not Found\n--------------------------------------------------------------------------------------\n\n")
        if context['expectations'] and len(context['expectations'].strip()) > 0:
            exp = get_forbidden_constraint(context['expectations'],apk)
            if 'not found' not in exp.lower():
                try:
                    chain = LLMChain(llm=llm, prompt=prompt_exp)
                    result = chain.run(expectations=exp, subsequent_events=effect_text)
                    print(result)
                    # if '"confidence": "high"' in result or '"confidence": "confirmed"' in result:
                    with open(f"res/detection/expectations/{apk}.log", "a") as file:
                        file.write(f"expectations:\n{exp}\n Subsequent events:\n{effect_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")

                except Exception as e:
                    print(f"error {e}")
                time.sleep(2)
            else:
                with open(f"res/detection/expectations/{apk}.log", "a") as file:
                    file.write(
                        f"expectations:\n{exp}\nConstraint Not Found\n--------------------------------------------------------------------------------------\n\n")
    return ""


def get_forbidden_events(effects):
    print(f"effects = {effects}")
    with open("data/forbiddens.log", "r") as file:
        data = json.load(file)
    for item in data:
        if item['content'] == effects:
            return item["forbidden"]
    return None

from difflib import SequenceMatcher

def get_closest_string(target, string_list):
    """
    Find the closest string in the list to the target string.

    Args:
        target (str): The string to compare against.
        string_list (list): A list of strings to find the closest match.

    Returns:
        str: The closest string from the list.
    """
    if not string_list:
        return None

    # Use SequenceMatcher to calculate similarity
    closest_string = max(string_list, key=lambda x: SequenceMatcher(None, target, x).ratio())
    return closest_string

def chain_detector_v2(apk):
    if not os.path.exists(f"res/context/{apk}.json"):
        return None

    with open(f'res/context/{apk}.json', 'r') as f:
        context_raw = f.read()

    with open(f'res/trace/{apk}.json', 'r') as f:
        trace_data = json.load(f)

    with open(f'res/profile/{apk}.log', 'r') as f:
        profile_data = f.read()

    context_raw = context_raw.replace("][", ",")
    context_js = json.loads(context_raw)
    contexts = sorted(context_js, key=lambda x: x['timestamp'])

    for context in contexts:
        if not "is_privacy_api" in context.keys() or not context["is_privacy_api"]:
            continue
        condition_text = ""
        effect_text = ""
        effect_list = []
        condition_list = []
        index_con = 1
        index_exp = 1
        for context2 in contexts:
            des = ""
            if "description" in context2.keys() and context2["description"]:
                des = f"{context2['description']};"
            if context2["timestamp"] < context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in condition_list:
                    condition_text += str(index_con) + ". " + des + context2["context"] + "\n"
                    condition_list.append(context2["context"])
                    index_con += 1
                # if "premise" in context.keys() and context["premise"] and context["premise"] not in premise_list:
                #     premise_text += context["premise"] + "\n"
                #     premise_list.append(context["premise"])
            elif context2["timestamp"] > context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in effect_list:
                    effect_text += str(index_exp) + ". " + des +context2["context"] + "\n"
                    effect_list.append(context2["context"])
                    index_exp += 1
        if context['context'] and len(context['context'].strip()) > 0:

            req = get_obligatory_constraint(context['context'], apk)
            if 'not found' not in req.lower():
                try:
                    chain = LLMChain(llm=llm, prompt=prompt_context)
                    condition_text = f"{profile_data}\n\n {condition_text}"
                    result = chain.run(requirements=req, context=condition_text)
                    with open(f"res/detection/context/{apk}.log", "a") as file:
                        file.write(
                            f"requirement:\n{req}\nContext:\n{condition_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")

                except Exception as e:
                    print(f"error {e}")
                time.sleep(2)
            else:
                with open(f"res/detection/context/{apk}.log", "a") as file:
                    file.write(
                        f"requirement:\n{req}\nConstraint Not Found\n--------------------------------------------------------------------------------------\n\n")
    for trace in trace_data:
        print(f"trace =  {trace}")
        if (not "is_privacy" in trace.keys() or not trace["is_privacy"]) or not tools.isPricacyAPI(trace['class_name'], trace['method']):
            continue
        condition_text = ""
        effect_text = ""
        effect_list = []
        condition_list = []
        index_con = 1
        index_exp = 1
        raw_effects = []
        arguments = str(trace['arguments'])
        raw_effects.append(trace['api_summary']['effects'])
        print(f"arguments = {arguments}")
        if 'parameter_configurations' in trace['api_summary'].keys():
            params = [str(item["parameter_values"]) for item in trace['api_summary']['parameter_configurations']]
            print(f"params = {params}")
            if params:
                best_match = get_closest_string(arguments, params)
                print(f"matches = {best_match}")
                if best_match:
                    for item in trace['api_summary']['parameter_configurations']:
                        if str(item["parameter_values"]) == best_match:
                            raw_effects.append(item["effects"])
        exp = ""
        for eff in raw_effects:
            res = get_forbidden_events(eff)
            if res:
                exp += str(res)
        print(f"exp = {exp}")

        for context2 in contexts:
            des = ""
            if "description" in context2.keys() and context2["description"]:
                des = f"{context2['description']};"
            if context2["timestamp"] < trace["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in condition_list:
                    condition_text += str(index_con) + ". " + des + context2["context"] + "\n"
                    condition_list.append(context2["context"])
                    index_con += 1
                # if "premise" in context.keys() and context["premise"] and context["premise"] not in premise_list:
                #     premise_text += context["premise"] + "\n"
                #     premise_list.append(context["premise"])
            elif context2["timestamp"] > trace["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in effect_list:
                    effect_text += str(index_exp) + ". " + des + context2["context"] + "\n"
                    effect_list.append(context2["context"])
                    index_exp += 1
        if exp:
            # exp = get_forbidden_constraint(context['expectations'],apk)
            if 'not found' not in exp.lower():
                try:
                    chain = LLMChain(llm=llm, prompt=prompt_exp)
                    result = chain.run(expectations=exp, subsequent_events=effect_text)
                    print(result)
                    # if '"confidence": "high"' in result or '"confidence": "confirmed"' in result:
                    with open(f"res/detection/expectations/{apk}.log", "a") as file:
                        file.write(f"expectations:\n{exp}\n Subsequent events:\n{effect_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")

                except Exception as e:
                    print(f"error {e}")
                time.sleep(2)
            else:
                with open(f"res/detection/expectations/{apk}.log", "a") as file:
                    file.write(
                        f"expectations:\n{exp}\nConstraint Not Found\n--------------------------------------------------------------------------------------\n\n")
    return ""

# test = get_forbidden_constraint("""
# disables personalized ads,
# personalized ads will not be displayed in the requested state,
# Only contextual ads can be displayed to the user,
# User data is not collected or sent,
# The SDK doesn't request consent from the user,
# Prevents the transmission of Android advertising identifier (AAID) and disables IBA and remarketing ads
# """, "test")
#
# print(test)
