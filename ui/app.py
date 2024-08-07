import streamlit as st
from rapid_law.components.graph_components.state import State
from rapid_law.components.graph_components import nodes as Node
from rapid_law.components.pinecone_utils import pinecone_query
from rapid_law.components.cohere_utils import cohere_text_generation
# from rapid_law.components.ollama_utils import ollama_text_generation
# from rapid_law.components.gemini_utils import gemini_text_generation
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
# from openai import OpenAI


graph_builder = StateGraph(State)

graph_builder.add_node("data_retrieval", Node.data_retrieval)
graph_builder.add_node("rerank", Node.rerank)
graph_builder.add_node("prompt_generation", Node.prompt_generation)
graph_builder.add_node("llm_node", Node.llm_node)

graph_builder.add_edge(START, "data_retrieval")
graph_builder.add_edge("data_retrieval", "rerank")
graph_builder.add_edge("rerank", "prompt_generation")
graph_builder.add_edge("prompt_generation", "llm_node")
graph_builder.add_edge("llm_node", END)

graph = graph_builder.compile()



st.title("💬 Legal AI For Bankruptcy Cases")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = graph.invoke({"messages": ("user", str(prompt))})
    # st.write(response)
    msg = response['messages'][-1].content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)