# PDF Query using OpenAI API

A simple solution for data retrieval from large PDF files

## Context
The OpenAI API introduces a new programmable approach for retrieving data from a raw text file using AI. We can easily create a prompt by combining raw text content and the data fields we wish to extract from the text. We then send this prompt to OpenAI in string format. By using a well-crafted prompt, we can also specify the desired response format, such as JSON or YAML, which greatly enhances the convenience of the extraction process. A great example exemplifying this is as follows:

Prompt:
```
Want to extract fields: "PO Number", "Total Amount" and "Delivery Address".
    Return result in JSON format without any explanation. 
    The PO content is as follows:
    %s
```
Note that the `%s` will be replaced by the raw text content and here is a sample output:
```
{
  "PO Number": "PO-003847945",
  "Total Amount": "1,485.00",
  "Delivery Address": "Peera Consumer Good Co.(QSC), P.O.Box 3371, Dohe, QAT"
}
```

## Problem
There is a limitation on the number of tokens that can be sent to the OpenAI API, and this applies not only to OpenAI but also to other LLM models. To put it simply, tokens can be thought of as words. For example, the token limit for `gpt-35-turbo` is 4096 tokens. That means the above approach doesn't work for the large text file (e.g. a file with 100 pages or even less)

## Solution
- Split the file into smaller chunks that are smaller than the token limitation.
- Utilize vector databases such as `FAISS` or `Chroma` to store these chunks.
- Use LLM to search for related chunks in the database for each data retrieval request and summarize the information to obtain the final result.

Refer to `chat.py` the details

## Run sample code
Prerequisites:
- Python 3.6+
- [Virtualenv](https://docs.python.org/3/library/venv.html)

Open terminal, move to the root directory and run the folllowing commands:
```
python -m venv .env
source .env/bin/activate
pip install -r /path/to/requirements.txt
```
Note that,
- the first command is only needed to run once to create `.env` folder in the root directory for the same code
- the second command is to activate the virtual env, need to run at the beginning of the test session
- the last command is to install dependencies, need to run once unless there're changes in dependencies

Next steps:
- update `chat.py` to add your open-ai API key
```
os.environ["OPENAI_API_KEY"] = "YOUR-OPEN-AI-API-KEY"
```
- run the code and ask questions
```
> python chat.py 
> Enter a query: what is the name of the document?
> The name of the document is the "Microsoft Partner Agreement".
> Enter a query: what is the legal entity in this document?
> The legal entity in this document is Microsoft.
```
