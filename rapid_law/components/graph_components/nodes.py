from rapid_law.components.pinecone_utils import pinecone_query
from langgraph.graph import StateGraph, START, END
from rapid_law.components.graph_components.state import State
from rapid_law.components.cohere_utils import cohere_text_generation,cohere_rerank
from rapid_law.components.format_to_xml import xml_format


def data_retrieval(state: State):
    response = pinecone_query("rapid-laws",state["messages"][0].content,top_k=10)
    docs = [matches['metadata'] for matches in response['matches']]
    return {"docs":docs}


# def prompt_generation(state: State):
#     context = '\n'.join([str(doc['section_content']) for doc in state["docs"]])
    
#     prompt = f"""
#     Act as a legal expert and provide a factual answer to the following question based on the provided documents.
#     Answer the question truthfully using the information provided in the documents. If the answer is not contained within the documents, say "I don't know" but if the user greets you then reply accordingly by ignoring the provided documents. Format your answer in markdown format.
#     Here are the relevant documents:
#     {context}

#     Based on the above documents, answer the following question:
#     {state["messages"][-1].content}
#     """

#     return {"prompt":str(prompt)}

def prompt_generation(state: State):
    context = xml_format(state["docs"])
    prompt = f"""
    Act as a legal expert and provide a factual answer to the following question based on the provided documents but If the user asks a general question not related to bankruptcy, provide a relevant and helpful answer based on your knowledge by ignoring the relevant document.
    You have access to an XML document containing details about bankruptcy law. The document is structured as follows:
    {context}

    If the question is related to bankruptcy, follow these instructions:

    Extract Relevant Information: Use the paragraphs within section_content from the XML document to answer the following question:
    Question:  {state["messages"][-1].content}
    Format Your Response: If the answer is not contained within the documents, respond with "I don't know." If the user greets you, reply accordingly by ignoring the provided documents.
    Citation Format: When citing information from the documents, include the title, chapter, and subchapter with the link taken from the url tag to embed in the title.
    Response Format:

    Your answer should be formatted in markdown and include a citation as follows:

    Answer: [Provide the answer here]
    Citation: Title, Chapter [Chapter Number], Subchapter [Subchapter Number]

    If the question is law-related but does not pertain to bankruptcy, respond by stating that such questions are outside the domain on which this LLM model is trained.
    """

    print(prompt)
    print('-'*50)
    return {"prompt":str(prompt)}


def llm_node(state: State):
    print(state['prompt'])
    response = cohere_text_generation(query=state['prompt'])
    return {"messages": str(response)}

def rerank(state: State):
    docs = cohere_rerank(query=state["messages"][-1].content,docs=state["docs"])
    return {"docs":docs}

def llm_node(state: State):
    print(state['prompt'])
    # response = gemini_text_generation(query=state['prompt'])
    # response = ollama_text_generation(query=state['prompt'],model_name='phi3')
    response = cohere_text_generation(query=state['prompt'])
    return {"messages": str(response)}

# graph_builder = StateGraph(State)

# graph_builder.add_node("data_retrieval", data_retrieval)

# graph_builder.add_edge(START, "data_retrieval")
# graph_builder.add_edge("data_retrieval", END)

# graph = graph_builder.compile()


# while True:
#     user_input = input("User: ")
#     if user_input.lower() in ["quit", "exit", "q"]:
#         print("Goodbye!")
#         break
#     for event in graph.stream({"messages": str(user_input)}):
#         for value in event.values():
#             print("Assistant:", value["docs"])