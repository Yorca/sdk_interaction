template = """
Given an app runtime context that logs conditions met and events triggered, and a list of privacy APIs with their respective summaries, can you identify any APIs that should be invoked based on both the runtime context and the conditions/effects outlined in the API summaries?

% context
{context}

% privacy APIs and summaries
{privacy_apis}

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
prompt = PromptTemplate(input_variables=["traces", "context_and_premise"],template=template)

with open('../traces5.json', 'r') as f:
    trace_data = json.load(f)

with open('../test_data/context5.json', 'r') as f:
    context = json.load(f)

chain = LLMChain(llm=llm, prompt=prompt)

apis = """
[
                {
                    "API_name": "SetMetaData",
                    "class_name": [
                        "com.unity3d.ads.metadata.MetaData"
                    ],
                    "conditions": [
                        "The user must express consent for targeted advertising."
                    ],
                    "effects": [
                        "Allows the developer to set user-specific metadata related to privacy preferences such as consent for targeted advertising.",
                        "Allows the passing of consent flags for data privacy laws compliance."
                    ],
                    "parameter_configurations": [
                        {
                            "parameter_values": [
                                "user.nonbehavioral",
                                "true"
                            ],
                            "conditions": [
                                "If the user opts out of personalized ads."
                            ],
                            "effects": [
                                "User will not receive personalized ads."
                            ]
                        },
                        {
                            "parameter_values": [
                                "user.nonbehavioral",
                                "false"
                            ],
                            "conditions": [
                                "If the user opts in to personalized ads."
                            ],
                            "effects": [
                                "User will receive personalized ads."
                            ]
                        },
                        {
                            "parameter_values": [
                                "pipl.consent",
                                "true"
                            ],
                            "conditions": [
                                "User opts in to sending their personal identifiable information outside of China."
                            ],
                            "effects": [
                                "Allows sending user's personal identifiable information as per PIPL compliance.",
                                "User consent is recorded for sending personal data."
                            ]
                        },
                        {
                            "parameter_values": [
                                "gdpr.consent",
                                "true"
                            ],
                            "conditions": [
                                "User opts in to targeted advertising under GDPR compliance."
                            ],
                            "effects": [
                                "User consents to receiving targeted advertisements."
                            ]
                        },
                        {
                            "parameter_values": [
                                "privacy.consent",
                                "true"
                            ],
                            "conditions": [
                                "User opts in to targeted advertising under various consumer privacy acts."
                            ],
                            "effects": [
                                "User agrees to receive personalized ads under specified consumer privacy acts."
                            ]
                        },
                        {
                            "parameter_values": [
                                "gdpr.consent",
                                "false"
                            ],
                            "conditions": [
                                "User opts out of targeted advertising under GDPR."
                            ],
                            "effects": [
                                "User consent is recorded against targeted advertising."
                            ]
                        },
                        {
                            "parameter_values": [
                                "pipl.consent",
                                "false"
                            ],
                            "conditions": [
                                "User opts out of sending their personal identifiable information outside of China."
                            ],
                            "effects": [
                                "User consent is recorded against sending personal data."
                            ]
                        }
                    ]
                }
                ]


"""



result = chain.run(context=context, privacy_apis=apis)


print(result)
with open("../res/missing_detection5-3.txt", "a") as file:
    file.write(result)