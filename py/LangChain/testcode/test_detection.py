template = """
I have a trace that records API calls, UI displays, button clicks, and other events. Each event has a timestamp and content (such as the displayed or clicked content, the called API and its parameters, etc.). I also have a context file, where each item contains the following three pieces of information:

Timestamp: The time when the context or premise starts to take effect.
Context: An event that has occurred or a condition that has been met.
Premise: Things that should or should not happen afterward


Task:
1. Traverse the trace from beginning to end. For each event, consider ALL contexts and premises with timestamps earlier than but not equal to the event's timestamp as the current event's context and premise.
2. Check whether the details of the events conflict with any premise or context, including inconsistencies in numerical ranges, logical conditions, semantics, and scope. Ensure that conditions are correctly interpreted and that overlapping or non-overlapping ranges are properly accounted for.
3. For events that include api_summary information, check whether the conditions for calling the API and setting parameters conflict with the current context.
4. Detect all potential inconsistency or logic flaw based on the current trace and the above context and premises

Examples:
1. If there is a premise before the current event's timestamp stating that location data should not be collected, but the current event is an API call that collects location data, identify this as an inconsistency.
2. If the current event is a call to the setGDPR method, and the api_summary specifies that this method needs to be called before classA's initialize, but the context shows that classA's initialize has already been called, then calling setGDPR afterward is an inconsistency.

Output:
Please perform the above detection and provide a list of all inconsistencies or conflicts found in the trace, along with explanations for each inconsistency."

% traces
{traces}

% total context and premise
{context_and_premise}

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

with open('../test_data/context5.json', 'r') as f:
    context = json.load(f)

chain = LLMChain(llm=llm, prompt=prompt)

result = chain.run(traces=trace_data, context_and_premise=context)
print(result)
with open("../res/detection5-5.txt", "a") as file:
    file.write(result)