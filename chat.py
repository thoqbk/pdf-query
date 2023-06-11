import os 
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.vectorstores import Chroma
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA


os.environ["OPENAI_API_KEY"] = ""

pdf_path = "./docs/ms-partner-agreement.pdf"

loader = PyMuPDFLoader(pdf_path)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=128)
texts = text_splitter.split_documents(documents)

# Chroma vector DB
# persist_directory = "./storage"
# embeddings = OpenAIEmbeddings()
# vectordb = Chroma.from_documents(documents=texts,  embedding=embeddings, persist_directory=persist_directory)
# vectordb.persist()
# retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# FAISS vector DB
embeddings = OpenAIEmbeddings()
index = FAISS.from_documents(texts, embeddings)
retriever = index.as_retriever()

llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

while True:
        user_input = input("Enter a query: ")
        if user_input == "exit":
            break

        query = f"###Prompt: {user_input}"
        try:
            llm_response = qa(query)
            print(llm_response["result"])
        except Exception as err:
            print('Exception occurred. Please try again', str(err))