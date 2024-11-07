template = """
I have a trace that records API calls, UI displays, button clicks, and other events. Each event has a timestamp and content (such as the displayed or clicked content, the called API and its parameters, etc.). I also have a context file, where each item contains the following three pieces of information:

Timestamp: The time when the context or premise starts to take effect.
Context: An event that has occurred or a condition that has been met.
Premise: Things that should or should not happen afterward


Task:
1. Check whether the details of the events conflict with any premise or context, including inconsistencies in numerical ranges, logical conditions, semantics, and scope. Ensure that conditions are correctly interpreted and that overlapping or non-overlapping ranges are properly accounted for.
2. For events that include api_summary information, check whether the conditions for calling the API and setting parameters conflict with the current context.
3. Detect all potential inconsistency or logic flaw based on the current trace and the above context and premises

Examples:
1. If there is a premise before the current event's timestamp stating that location data should not be collected, but the current event is an API call that collects location data, identify this as an inconsistency.
2. If the current event is a call to the setGDPR method, and the api_summary specifies that this method needs to be called before classA's initialize, but the context shows that classA's initialize has already been called, then calling setGDPR afterward is an inconsistency.

Output:
Please perform the above detection and provide a list of all inconsistencies or conflicts found in the trace, along with explanations for each inconsistency."

% trace
{trace}

% context
{context}

% premise
{premise}

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
    contexts = json.load(f)

for trace in trace_data:
    context_text = ""
    premise_text = ""
    for context in contexts:
        if context["timestamp"] < trace["timestamp"]:
            if "context" in context.keys():
                context_text += context["context"] + "\n"
            if "premise" in context.keys():
                premise_text += context["premise"] + "\n"
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(trace=trace, context=context_text, premise=premise_text)
    print(result)
    with open("../res/pipeline_detection5-5.txt", "a") as file:
        file.write(f"Context:\n{context_text}\nPremise:\n{premise_text}\nResults:\n{result}\n--------------------------------------------------------------------------------------\n")
