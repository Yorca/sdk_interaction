template = """
I have a trace that records API calls, UI displays, button clicks, and other events in the running of an app. Each event has a timestamp and content (such as the displayed or clicked content, the called API and its parameters, etc.). I also have a context file, where each item contains the following three pieces of information:

Timestamp: The time when the context or premise starts to take effect.
Context: An event that has occurred or a condition that has been met.
Premise: Things that should or should not happen afterward

I will also provide you the profile of the APP, which is the information they declared on Google Play, along with some runtime environment information.


Task:
1. Check whether the details of the events conflict with the app's profile, any premise or context, including inconsistencies in numerical ranges, logical conditions, semantics, and scope. Ensure that conditions are correctly interpreted and that overlapping or non-overlapping ranges are properly accounted for.
2. For events that include api_summary information, check whether the conditions for calling the API and setting parameters conflict with the current context.
3. Detect whether the action/purpose of the detection method conflicts with the existing premise. 
4. Detect all potential inconsistency or logic flaw based on the current trace and the above context and premises

Examples:
1. If there is a premise before the current event's timestamp stating that location data should not be collected, but the current event is an API call that collects location data, identify this as an inconsistency.
2. If the current event is a call to the setGDPR method, and the api_summary specifies that this method needs to be called before classA's initialize, but the context shows that classA's initialize has already been called, then calling setGDPR afterward is an inconsistency.

Output:
Please perform the above detection and provide a list of all inconsistencies or conflicts found in the trace, along with explanations for each inconsistency. If no inconsistencies or conflicts are found, output 'not found'

format:

% app profile
{app_profile}

% trace
{trace}

% context
{context}

% premise
{premise}

"""


template_v2 = """
You are an inconsistency detector for privacy APIs. I will provide you with the following information:
1. Privacy API: Details of the invoked privacy API, including its runtime information (parameters, return values, etc.) and a summary extracted from the official developer documentation.
2. Running Environment and App Profile: Information about the app's execution environment and profile.
3. Context: Events that occurred before the API invocation.
4. Subsequent Events: Events that occurred after the API invocation.

Your Task: Detect inconsistencies between the privacy API's documented behavior (from its summary) and its actual observed behavior.

Instructions:
1. Consider the running environment, app profile, and context as the overall context. Read the API's summary (in the api_summary field) thoroughly. Based on the conditions required for invoking the API and for setting its parameters (if applicable), detect any inconsistencies between the overall context and these conditions.
2. Based on the expected effects of the API invocation and its parameters, detect any inconsistencies between the subsequent events and these expected effects.
3. Inconsistencies include, but are not limited to, discrepancies in numerical ranges, logical conditions and requirements, sequences, semantics, and scope. Ensure that conditions are correctly interpreted and that overlapping or non-overlapping ranges are properly accounted for.
4. Please perform the above detection and provide a list of all inconsistencies or conflicts found, along with explanations for each. If no inconsistencies or conflicts are found, output 'not found'.

Output Format:
Please output a list of dictionaries for each detected inconsistency:
[
    {{
        "inconsistency": "", // Overview of the inconsistency. If no inconsistencies are found, output "not found".
        "reference": "",     // The involved conditions/effects and context/subsequent events.
        "description": "Explain why this is an inconsistency."
    }}
]

% privacy API
{trace}

% running environment and app profile
{app_profile}

% context
{context}

% Subsequent Events
{subsequent_events}

"""

template_v3 = """
You are an inconsistency detector for privacy APIs. I will provide you the following information:

1. Privacy API:  Details of the invoked privacy API, including its runtime information (parameters, return values, etc.), its conditions (conditions that need to be met before calling the method with the corresponding parameters), and its expectations (what should or should not happen afterward).
2. Running Environment and App Profile: The environment in which the app is running and the app's important properties.
3. Context: Events that occurred before this API invocation.
4. Subsequent Events:  Events that occurred after the API invocation.

Your Task: Detect inconsistencies between the privacy API's documented behavior (from its summary) and its actual observed behavior.

Instructions:
1. Understand the conditions of this API, and then iterate over the context to check if the context matches these conditions. If there are any inconsistencies or conflicts, report them.
2. Understand the expectations of this API, and then iterate over the subsequent events to check if these events match the expectations. If there are any inconsistencies or conflicts, report them.
3. Inconsistencies include, but are not limited to, discrepancies in numerical ranges, logical conditions and requirements, sequences, semantics, and scope. Ensure that conditions are correctly interpreted and that overlapping or non-overlapping ranges are properly accounted for.
4. Please perform the above detection and provide a list of all inconsistencies or conflicts found, along with explanations for each. 
5. If no inconsistencies or conflicts are found, output 'not found'.

Output Format:
If you found inconsistencies/conflicts, please output a list of dictionaries for each detected inconsistency:
[
    {{
        "inconsistency": "", // Overview of the inconsistency.
        "reference": "",     // The involved conditions/effects and context/subsequent events.
        "description": "Explain why this is an inconsistency."
    }}
]

If you do no found any inconsistency, output "not found"

% privacy API
{trace}

% running environment and app profile
{app_profile}

% context
{context}

% Subsequent Events
{subsequent_events}

"""

template_context = """
You are an inconsistency detector for privacy APIs. I will provide you the following information:

1. Privacy API:  Details of the invoked privacy API, including its runtime information (parameters, return values, etc.) and its conditions (conditions that need to be met before calling the method with the corresponding parameters)
2. Running Environment and App Profile: The environment in which the app is running and the app's important properties.
3. Context: Events that occurred before this API invocation.

Your Task: Detect inconsistencies between the privacy API's documented behavior (from its summary) and its actual observed behavior.

Instructions:
1. Understand the conditions of this API, and then iterate over the context to check if the context matches these conditions. If there are any inconsistencies or conflicts, report them.
2. Inconsistencies include, but are not limited to, discrepancies in numerical ranges, logical conditions and requirements, sequences, semantics, and scope. Ensure that conditions are correctly interpreted and that overlapping or non-overlapping ranges are properly accounted for.
3. Please perform the above detection and provide a list of all inconsistencies found, along with explanations for each. 
5. If no inconsistencies or conflicts are found, output 'not found'.

Output Format:
If you found inconsistencies/conflicts, please output a list of dictionaries for each detected inconsistency:
[
    {{
        "inconsistency": "", // Overview of the inconsistency.
        "reference": "",     // The involved conditions/effects and context/subsequent events.
        "description": "Explain why this is an inconsistency."
    }}
]

If you do no found any inconsistency, output "not found"

% privacy API
{trace}

% running environment and app profile
{app_profile}

% context
{context}

"""


template_expectation = """
You are an inconsistency detector for privacy APIs. I will provide you the following information:

1. Privacy API:  Details of the invoked privacy API, including its runtime information (parameters, return values, etc.), and its expectations (what should or should not happen afterward).
2. Subsequent Events:  Events that occurred after the API invocation.

Your Task: Detect inconsistencies between the privacy API's documented behavior (from its summary) and its actual observed behavior.

Instructions:
1. Understand the expectations of this API, and then iterate over the subsequent events to check if these events match the expectations. If there are any inconsistencies or conflicts, report them.
2. Inconsistencies include, but are not limited to, discrepancies in numerical ranges, logical conditions and requirements, sequences, semantics, and scope. Ensure that conditions are correctly interpreted and that overlapping or non-overlapping ranges are properly accounted for.
3. Please perform the above detection. If you found issues, please provide a list of all inconsistencies or conflicts found, along with explanations for each. 
4. If no inconsistencies or conflicts are found, output 'not found'.

Output Format:
If you found inconsistencies/conflicts, please output a list of dictionaries for each detected inconsistency:
[
    {{
        "inconsistency": "", // Overview of the inconsistency.
        "reference": "",     // The involved conditions/effects and context/subsequent events.
        "description": "Explain why this is an inconsistency."
    }}
]

If you do no found any inconsistency, output "not found"

% privacy API
{trace}

% Subsequent Events
{subsequent_events}

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
llm = ChatOpenAI(model_name="gpt-4o-mini", api_key=os.getenv('OPENAI_API_KEY'))
prompt = PromptTemplate(input_variables=["profile_data", "traces", "context_text", "premise_text"],template=template)
prompt_v2 = PromptTemplate(input_variables=["trace", "app_profile", "context", "subsequent_events"],template=template_v2)
prompt_v3 = PromptTemplate(input_variables=["trace", "app_profile", "context", "subsequent_events"],template=template_v3)

prompt_context = PromptTemplate(input_variables=["trace", "app_profile", "context"],template=template_context)
prompt_exp = PromptTemplate(input_variables=["trace", "subsequent_events"],template=template_expectation)
def detect(apk):
    if not os.path.exists(f"res/trace/{apk}.json") or not os.path.exists(f"res/context/{apk}.json"):
        return None
    print(apk)
    with open(f'res/trace/{apk}.json', 'r') as f:
        trace_data = json.load(f)

    with open(f'res/context/{apk}.json', 'r') as f:
        context_raw = f.read()

    with open(f'res/profile/{apk}.log', 'r') as f:
        profile_data = f.read()

    context_raw = context_raw.replace("][", ",")
    context_js = json.loads(context_raw)
    contexts = sorted(context_js, key=lambda x: x['timestamp'])

    skip_index = []

    for i in range(len(trace_data)):
        if i in skip_index:
            continue
        trace =trace_data[i]
        if trace["event_type"] != "method call":
            continue
        if trace["source"] == "normal" and not trace["is_privacy"]:
            continue
        context_text = ""
        premise_text = ""
        context_list = []
        premise_list = []
        for context in contexts:
            if context["timestamp"] < trace["timestamp"]:
                if "context" in context.keys() and context["context"] and context["context"] not in context_list:
                    context_text += context["context"] + "\n"
                    context_list.append(context["context"])
                if "premise" in context.keys() and context["premise"] and context["premise"] not in premise_list:
                    premise_text += context["premise"] + "\n"
                    premise_list.append(context["premise"])

        traces = [trace]
        if trace["source"] == "sensitive":
            j = i + 1
            while j < len(trace_data) and "source" in trace_data[j].keys() and trace_data[j]["source"] == "sensitive": # batch detect
                traces.append(trace_data[j])
                skip_index.append(j)
                j += 1
        try:
            chain = LLMChain(llm=llm, prompt=prompt)
            result = chain.run(app_profile= profile_data, trace=traces, context=context_text, premise=premise_text)
            print(result)
            with open(f"res/detection/{apk}.log", "a") as file:
                file.write(f"Trace:\n{traces}\nContext:\n{context_text}\nPremise:\n{premise_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")
        except Exception as e:
            print(f"error {e}")
    return ""




def detect_v2(apk):
    if not os.path.exists(f"res/trace/{apk}.json") or not os.path.exists(f"res/context/{apk}.json"):
        return None
    print(apk)
    with open(f'res/trace/{apk}.json', 'r') as f:
        trace_data = json.load(f)

    with open(f'res/context/{apk}.json', 'r') as f:
        context_raw = f.read()

    with open(f'res/profile/{apk}.log', 'r') as f:
        profile_data = f.read()

    context_raw = context_raw.replace("][", ",")
    context_js = json.loads(context_raw)
    contexts = sorted(context_js, key=lambda x: x['timestamp'])

    for trace in trace_data:
        if trace["event_type"] != "method call":
            continue
        if not trace["is_privacy"]:
            continue
        context_text = ""
        condition_text = ""
        premise_text = ""
        effect_text = ""
        context_list = []
        premise_list = []
        effect_list = []
        condition_list = []
        for context in contexts:
            if context["timestamp"] < trace["timestamp"]:
                if "context" in context.keys() and context["context"] and context["context"] not in condition_list:
                    condition_text += context["context"] + "\n"
                    condition_list.append(context["context"])
                # if "premise" in context.keys() and context["premise"] and context["premise"] not in premise_list:
                #     premise_text += context["premise"] + "\n"
                #     premise_list.append(context["premise"])
            elif context["timestamp"] > trace["timestamp"]:
                if "context" in context.keys() and context["context"] and context["context"] not in effect_list:
                    effect_text += context["context"] + "\n"
                    effect_list.append(context["context"])

        # traces = [trace]
        # if trace["source"] == "sensitive":
        #     j = i + 1
        #     while j < len(trace_data) and "source" in trace_data[j].keys() and trace_data[j]["source"] == "sensitive": # batch detect
        #         traces.append(trace_data[j])
        #         skip_index.append(j)
        #         j += 1
        try:
            chain = LLMChain(llm=llm, prompt=prompt_v2)
            result = chain.run(trace=trace, app_profile=profile_data, context=condition_text, subsequent_events=effect_text)
            print(result)
            with open(f"res/detection/{apk}.log", "a") as file:
                file.write(f"Trace:\n{trace}\nContext:\n{condition_text}\nPremise:\n{effect_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")
        except Exception as e:
            print(f"error {e}")
    return ""

def detect_v3(apk):
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
        for context2 in contexts:
            if context2["timestamp"] < context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in condition_list:
                    condition_text += context2["context"] + "\n"
                    condition_list.append(context2["context"])
                # if "premise" in context.keys() and context["premise"] and context["premise"] not in premise_list:
                #     premise_text += context["premise"] + "\n"
                #     premise_list.append(context["premise"])
            elif context2["timestamp"] > context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in effect_list:
                    effect_text += context2["context"] + "\n"
                    effect_list.append(context2["context"])

        trace = f"{context['description']}; Conditions: {context['context']}; Expectations: {context['expectations']}"
        try:
            chain = LLMChain(llm=llm, prompt=prompt_v3)
            result = chain.run(trace=trace, app_profile=profile_data, context=condition_text, subsequent_events=effect_text)
            print(result)
            with open(f"res/detection/{apk}.log", "a") as file:
                file.write(f"Trace:\n{trace}\nContext:\n{condition_text}\nPremise:\n{effect_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")
        except Exception as e:
            print(f"error {e}")
    return ""


def detect_v4(apk):
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
        for context2 in contexts:
            if context2["timestamp"] < context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in condition_list:
                    condition_text += context2["context"] + "\n"
                    condition_list.append(context2["context"])
                # if "premise" in context.keys() and context["premise"] and context["premise"] not in premise_list:
                #     premise_text += context["premise"] + "\n"
                #     premise_list.append(context["premise"])
            elif context2["timestamp"] > context["timestamp"]:
                if "context" in context2.keys() and context2["context"] and context2["context"] not in effect_list:
                    effect_text += context2["context"] + "\n"
                    effect_list.append(context2["context"])

        trace_context = f"{context['description']}; Conditions: {context['context']}"
        trace_expectations = f"{context['description']}; Expectations: {context['expectations']}"
        try:
            chain = LLMChain(llm=llm, prompt=prompt_context)
            result = chain.run(trace=trace_context, app_profile=profile_data, context=condition_text)
            print(result)
            with open(f"res/detection/context/{apk}.log", "a") as file:
                file.write(f"Trace:\n{trace_context}\nContext:\n{condition_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")
        except Exception as e:
            print(f"error {e}")

        try:
            chain = LLMChain(llm=llm, prompt=prompt_exp)
            result = chain.run(trace=trace_expectations, subsequent_events=effect_text)
            print(result)
            with open(f"res/detection/expectations/{apk}.log", "a") as file:
                file.write(f"Trace:\n{trace_expectations}\nContext:\n Subsequent events:\n{effect_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n\n")
        except Exception as e:
            print(f"error {e}")
    return ""