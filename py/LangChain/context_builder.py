template = """
 You are a context/expectations summarizer. You will be provided with a runtime trace log of an app, which is a list of dictionaries capturing method calls, UI displays, and view click events during the app's execution. Your task is to process each event and produce a summary in JSON format.
 Instructions:
 1. Iterate over the runtime trace, which is a list of dictionaries, and summarize every event.
 2. For events where `event_type` is **"method call"**:
    - If `is_privacy` is `true`, it indicates a privacy API.
    - Briefly describe the method call, including the method name, class name, arguments, and return value.
    - If the API does not have a parameter, just summarize the conditions and effects of invoking the API.
    - If the API has parameters, read the runtime arguments settings ("arguments" field) , match and get its corresponding conditions and effects from "parameter_configurations" field
    - Based on the matching result:
        - a). If you found the parameter settings that match arguments ,summarize the conditions into the context, and summarize the effects into expectations. You need to cover all information mentioned in "condition" or "effects" fields of the corresponding parameter setting and the API.
        - b). If no matching parameter configuration is found (for example, the API was called with parameter "-1" in runtime, but you can not find the description of "-1" in parameter_configurations field): Leave both the context and expectation fields blank.
    - Example:
      **Input:**
      {{
        "method": "setCoppa",
        "class_name": "io.bidmachine.BidMachine",
        "timestamp": 1730237721633,
        "arguments": "{{\"0\":true}}",
        "is_privacy": true,
        "return": "undefined",
        "api_summary": {{
          "conditions": ["You need to ensure compliance with COPPA."],
          "effects": ["Indicates whether a user falls within an age-restricted category as per COPPA requirements.", "Specifies whether COPPA regulations apply for the current user."],
          "parameter_configurations": [
            {{
              "parameter_values": [true],
              "conditions": ["The user is under the age of 13."],
              "effects": ["Indicates that the user is under the age of 13 and is subject to COPPA regulations.", "The SDK will treat the user as a child under COPPA regulations."]
            }},
            {{
              "parameter_values": [false],
              "conditions": ["User is 13 years of age or older."],
              "effects": ["Indicates that the user is not under the age of 13 and is not subject to COPPA regulations.", "No restrictions based on COPPA for this user."]
            }}
          ]
        }},
        "event_type": "method call"
      }}

      **Output:**
      {{
        "timestamp": 1730237721633,
        "is_privacy_api": true,
        "description": "call 'setCoppa" of class 'io.bidmachine.BidMachine' with arguments 'false', return undefined",
        "context": "You need to ensure compliance with COPPA and the user is under the age of 13.",
        "expectations": "The user is subject to COPPA regulations. The SDK will treat the user as a child under COPPA regulations."
      }}
      
 3. For events where `event_type` is **"UI display"**:
    - This is the text displayed on the screen, please describe what is displayed on the screen based on the content field.
    - Example:
      **Input:**
      {{
        "timestamp": 1728947141601,
        "content": "Tundra is asking for permission to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, in order to show you relevant ads. This will provide you with an enhanced advertising experience. By agreeing, you confirm that you are over 16 years old and would like to personalize your ad experience. The purposes include information storage and access, personalization, and ad selection, delivery, and reporting. This is powered by Appodeal.",
        "event_type": "UI Display"
      }}

      **Output:**
      {{
        "timestamp": 1728947141601,
        "context": "Display: Tundra displays a dialog asking for consent to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, for relevant ads."
      }}

 4. For events where `event_type` is **"View Click"**:
    - Summarize the clicked content and the context in which it occurred, based on the clicked_text and page content fields.
    - Example:
      **Input:**
      {{
        "timestamp": 1730237797875,
        "clicked_text": "agree",
        "page content": "Tundra is asking for permission to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, in order to show you relevant ads. This will provide you with an enhanced advertising experience. By agreeing, you confirm that you are over 16 years old and would like to personalize your ad experience. The purposes include information storage and access, personalization, and ad selection, delivery, and reporting. This is powered by Appodeal.",
        "event_type": "View Click"
      }}

      **Output:**
      {{
        "timestamp": 1730237797875,
        "context": "clicked "agree" in a dialog/page asking for consent to personalize advertising by collecting and processing personal data. The user agreed to personal data collection."
      }}
    
    1. Please output the summaries in JSON format, as shown in the examples, which can be directly parsed.
    2. You should process all the traces provided and convert them into the corresponding context.
    
    Process the following traces:
    {traces}

 """

template_v2 = """
 You are a context/expectations summarizer. You will be provided with a runtime trace log of an app, which is a list of dictionaries capturing UI displays, and view click events during the app's execution. Your task is to process each event and produce a summary in JSON format.
 Instructions:
 1. Iterate over the runtime trace, which is a list of dictionaries, and summarize every event.
 
 2. For events where `event_type` is **"UI display"**:
    - This is the text displayed on the screen, please describe what is displayed on the screen based on the content field.
    - Example:
      **Input:**
      {{
        "timestamp": 1728947141601,
        "content": "Tundra is asking for permission to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, in order to show you relevant ads. This will provide you with an enhanced advertising experience. By agreeing, you confirm that you are over 16 years old and would like to personalize your ad experience. The purposes include information storage and access, personalization, and ad selection, delivery, and reporting. This is powered by Appodeal.",
        "event_type": "UI Display"
      }}

      **Output:**
      {{
        "timestamp": 1728947141601,
        "context": "Display: Tundra displays a dialog asking for consent to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, for relevant ads."
      }}

 3. For events where `event_type` is **"View Click"**:
    - Summarize the clicked content and the context in which it occurred, based on the clicked_text and page content fields.
    - Example:
      **Input:**
      {{
        "timestamp": 1730237797875,
        "clicked_text": "agree",
        "page content": "Tundra is asking for permission to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, in order to show you relevant ads. This will provide you with an enhanced advertising experience. By agreeing, you confirm that you are over 16 years old and would like to personalize your ad experience. The purposes include information storage and access, personalization, and ad selection, delivery, and reporting. This is powered by Appodeal.",
        "event_type": "View Click"
      }}

      **Output:**
      {{
        "timestamp": 1730237797875,
        "context": "clicked "agree" in a dialog/page asking for consent to personalize advertising by collecting and processing personal data. The user agreed to personal data collection."
      }}

    1. Please output the summaries in JSON format, as shown in the examples, which can be directly parsed.
    2. You should process all the traces provided and convert them into the corresponding context.

    Process the following traces:
    {traces}

 """

from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import json
from langchain.chains import LLMChain
from langchain import OpenAI
import tools
import demjson3

llm = ChatOpenAI(model_name="gpt-4o-mini")



def get_context(pkg, traces):

    gpt_sum_list = []
    context_list = []
    for i in range(len(traces)):
        trace = traces[i]
        if (trace["event_type"] == "method call" and tools.isPricacyAPI(trace['class_name'], trace['method'])) or trace["event_type"] == "UI Display" or trace["event_type"] == "View Click":
            gpt_sum_list.append(trace)

        elif trace["event_type"] == "method call":
            return_content = trace['return']
            length_threshold = 50
            if len(trace['return']) > length_threshold:
                return_content = trace['return'][:length_threshold]
            if len(trace['arguments']) > length_threshold:
                return_content = trace['return'][:length_threshold]
            action = ""
            if "action" in trace.keys():
                action = f" to {trace['action']}"
            context_list.append({
                "timestamp": trace["timestamp"],
                "context": f"Call method {trace['method']} of Class {trace['class_name']}{action}; with parameters {trace['arguments']}; return {return_content}"
            })
        # elif trace["event_type"] == "View Click":
        #     context_list.append({
        #         "timestamp": trace["timestamp"],
        #         "context": trace["event"]
        #     })


    propmt = PromptTemplate(input_variables=["traces"], template=template)
    chain = LLMChain(llm=llm, prompt=propmt)
    result = chain.run(traces=gpt_sum_list)
    result = result.replace("```json\n", "").replace("\n```", "")
    try:
        with open(f"res/llm_context/{pkg}.json", "a") as file:
            file.write(json.dumps(result, indent=4))
    except:
        with open(f"res/llm_context/{pkg}.txt", "a") as file:
            file.write(result)
    print(result)
    js_result = demjson3.decode(result)

    contexts = sorted(context_list + js_result, key=lambda x: x['timestamp'])
    try:
        with open(f"res/context/{pkg}.json", "a") as file:
            file.write(json.dumps(contexts, indent=4))
    except:
        with open(f"res/context/{pkg}.txt", "a") as file:
            file.write(contexts)
    return contexts

#
# def get_context_v2(pkg, traces):
#
#     gpt_sum_list = []
#     context_list = []
#     for i in range(len(traces)):
#         trace = traces[i]
#         if trace["event_type"] == "UI Display" or trace["event_type"] == "View Click":
#             gpt_sum_list.append(trace)
#
#         elif trace["event_type"] == "method call":
#             return_content = trace['return']
#             length_threshold = 50
#             if len(trace['return']) > length_threshold:
#                 return_content = trace['return'][:length_threshold]
#             if len(trace['arguments']) > length_threshold:
#                 return_content = trace['return'][:length_threshold]
#             action = ""
#             if "action" in trace.keys():
#                 action = f" to {trace['action']}"
#             api_context = {
#                 "timestamp": trace["timestamp"],
#                 "context": f"Call method {trace['method']} of Class {trace['class_name']}{action}; with parameters {trace['arguments']}; return {return_content}"
#             }
#             if trace["is_privacy"]:
#                 api_context["is_privacy"] =
#             context_list.append({
#                 "timestamp": trace["timestamp"],
#                 "context": f"Call method {trace['method']} of Class {trace['class_name']}{action}; with parameters {trace['arguments']}; return {return_content}"
#             })
#
#
#     propmt = PromptTemplate(input_variables=["traces"], template=template)
#     chain = LLMChain(llm=llm, prompt=propmt)
#     result = chain.run(traces=gpt_sum_list)
#     result = result.replace("```json\n", "").replace("\n```", "")
#     try:
#         with open(f"res/llm_context/{pkg}.json", "a") as file:
#             file.write(json.dumps(result, indent=4))
#     except:
#         with open(f"res/llm_context/{pkg}.txt", "a") as file:
#             file.write(result)
#
#     js_result = json.loads(result)
#
#     contexts = sorted(context_list + js_result, key=lambda x: x['timestamp'])
#     try:
#         with open(f"res/context/{pkg}.json", "a") as file:
#             file.write(json.dumps(contexts, indent=4))
#     except:
#         with open(f"res/context/{pkg}.txt", "a") as file:
#             file.write(contexts)
#     return contexts
