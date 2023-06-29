# PDF Query

A simple code for data retrival from a large PDF file

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
python chat.py 
Enter a query: what is the name of the document?
The name of the document is the "Microsoft Partner Agreement".
Enter a query: what is the legal entity in this document?
The legal entity in this document is Microsoft.
```