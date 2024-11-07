template = """
 You are a summarizer. You will be provided with a runtime trace log of an app, capturing method calls, UI displays, and view click events during the app's execution. Your task is to summarize each event's context and premise(if any).

 Instructions:
 1. Iterate over the runtime trace, which is a list of dictionaries, and summarize every event. You should summarize the context and premise of each event/trace as detailed as possible.
 2. For events where `event_type` is **"method call"**:
    - If `is_privacy` is `true`, it indicates a privacy API. Use the `method`, `arguments`, and `conditions` fields to summarize the context. For the premise, use the `effects` field.
    - Example:
      **Input:**
      ```json
      {{
        "method": "setCoppa",
        "class_name": "io.bidmachine.BidMachine",
        "timestamp": 1730237721633,
        "arguments": "{{\"0\":true}}",
        "is_privacy": true,
        "api_summary": {{
          "conditions": ["To help ensure compliance with COPPA you must indicate whether a user falls within an age-restricted category."],
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
      ```

      **Output:**
      ```json
      {{
        "timestamp": 1730237721633,
        "context": "set Coppa to true. The user is under the age of 13.",
        "premise": "The user is under the age of 13 and is subject to COPPA regulations. The SDK will treat the user as a child under COPPA regulations."
      }}
      ```

    - If `is_privacy` is `false`, summarize only the context using the `method` and `arguments` fields. No premise is needed.
 3. For events where `event_type` is **"UI display"**:
    - Summarize the content of the display as the context.
    - Example:
      **Input:**
      ```json
      {{
        "timestamp": 1728947141601,
        "content": "Tundra is asking for permission to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, in order to show you relevant ads. This will provide you with an enhanced advertising experience. By agreeing, you confirm that you are over 16 years old and would like to personalize your ad experience. The purposes include information storage and access, personalization, and ad selection, delivery, and reporting. This is powered by Appodeal.",
        "event_type": "UI Display"
      }}
      ```

      **Output:**
      ```json
      {{
        "timestamp": 1728947141601,
        "context": "Tundra displays a dialog asking for consent to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, for relevant ads."
      }}
      ```

 4. For events where `event_type` is **"View Click"**:
    - Summarize the clicked content and the context in which it occurred.
    - Example:
      **Input:**
      ```json
      {{
        "timestamp": 1730237797875,
        "clicked_text": "agree",
        "page_content": "Tundra is asking for permission to personalize your advertising experience by collecting and processing personal data, such as device identifiers and location data, in order to show you relevant ads. This will provide you with an enhanced advertising experience. By agreeing, you confirm that you are over 16 years old and would like to personalize your ad experience. The purposes include information storage and access, personalization, and ad selection, delivery, and reporting. This is powered by Appodeal.",
        "event_type": "View Click"
      }}
      ```

      **Output:**
      ```json
      {{
        "timestamp": 1730237797875,
        "context": "The 'agree' button was clicked in a dialog asking for consent to personalize advertising by collecting and processing personal data. The user agreed to personal data collection."
      }}
      ```
      
    Process the following traces:
    {traces}
    
    Provide the output in JSON format as per the instructions.

 """


from langchain.document_loaders import UnstructuredFileLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import json
from langchain.chains import LLMChain
from langchain import OpenAI
llm = ChatOpenAI(model_name="gpt-4o-mini")
propmt = PromptTemplate(input_variables=["traces"],template=template)
# loader = UnstructuredFileLoader("../traces.json")
# document = loader.load()
# print(f'documents:{len(document)}')
#
# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500,
#     chunk_overlap=0
# )
#
# split_documents = text_splitter.split_documents(document)
# print(f'documents:{len(split_documents)}')

# llm = OpenAI(model_name="text-davinci-003", max_tokens=1500)
with open('../traces5.json', 'r') as f:
    trace_data = json.load(f)

chain = LLMChain(llm=llm, prompt=propmt)

result = chain.run(traces=trace_data)
print(result)