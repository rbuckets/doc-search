import constants

import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain.agents import load_tools
from langchain.agents import ZeroShotAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain import LLMChain

os.environ["OPENAI_API_KEY"] = constants.OPENAI_KEY

# Support for one pdf document: Replace path
loader = PyPDFLoader("./data/attention.pdf")
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 512,
    chunk_overlap  = 20,
)
chunks = loader.load_and_split(text_splitter)

# Create embedding model and llm
llm = ChatOpenAI(temperature=0.1)
embeddings = OpenAIEmbeddings()

# Create vector database and retriever
db = FAISS.from_documents(chunks, embeddings)
retriever = db.as_retriever()

# Create paper-searching tool (called tool_paper)
tool_paper = create_retriever_tool(
    retriever,
    "search_papers",
    "Searches through the papers for information regarding the prompt. If you've looked through all the papers and need additional info, then use the search tool as a last resort."
)

# create toolkit (with search tool)
toolkit = [
    tool_paper,
    load_tools(["serpapi"],
               llm=llm,
               serpapi_api_key="fe705be3a03c2fdfb40aa28344a6259a02f35437e0e74fad6c6d93d6e34c71fa")[0]
]
toolkit[1].description = "A search engine. Used when you need to look up outside information not provided in the papers. Input should be a search query. Only use if you searched through the papers and didn't find any information."

# writing prompt
prefix = """Have a conversation with a human, answering it's questions about papers. You have access to the following tools:"""
suffix = """Gather information found in the papers using the search_papers tool, then, if needed, look up additional information using the Search tool. Begin!"

{chat_history}
Question: {input}
{agent_scratchpad}"""

# create prompt and memory
prompt = ZeroShotAgent.create_prompt(
    tools=toolkit,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "chat_history", "agent_scratchpad"],
)
memory = ConversationBufferMemory(memory_key="chat_history")

# create agent and agent chain
llm_chain = LLMChain(llm=OpenAI(temperature=0.1), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain,
                      tools=toolkit,
                      agent="chat-conversational-react-description",
                      verbose=True)
agent_chain = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=toolkit, verbose=True, memory=memory
)

# instantiate chatbot
print("Welcome to the Transformers chatbot! Type 'exit' to stop.")

while True:
    query = input("Please enter your question: ")

    print(type(query))

    if query.lower() == 'exit':
        print("Thank you for using the State of the Union chatbot!")
        break

    result = agent_chain({"input": query.strip()})
    print(result["output"])
    print(f'User: {query}')
    print(f'Chatbot: {result["output"]}')

memory.clear()
