import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.agent.openai import OpenAIAgent
import streamlit as st
from constants import ( APIKEY )
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# set environment variable
os.environ["OPENAI_API_KEY"] = APIKEY

# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("Data/", recursive=True).load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
# either way we can now query the index
query_engine = index.as_query_engine(respose_length=100000)
query_engine_tools = [
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name="lyft_10k",
            description=(
                "Provides information about Lyft financials for year 2021. "
                "Use a detailed plain text question as input to the tool."
            ),
        ),
    )
]
# initialize llm
agent = OpenAIAgent.from_tools(query_engine_tools, verbose=True)
question = None
user = st.chat_message("Human")
bot = st.chat_message("AI")
prompt = st.chat_input("Ask a question: ")
user.write(prompt)
query_engine = agent.query_engine
if prompt:
    response = query_engine.query(prompt)
    bot.write(str(response))
