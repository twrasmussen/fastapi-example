# Setup Steps
## Install dependendencies 
pip install "fastapi[all]" \
pip freeze > requirements.txt

## Run 
uvicorn main:app --reload
Note: \

The command uvicorn main:app refers to: \
main: the file main.py (the Python "module"). \
app: the object created inside of main.py with the line app = FastAPI(). \
--reload: make the server restart after code changes. Only use for development. \

Open your browser at http://127.0.0.1:8000. \
You will see the JSON response as: \
{"message": "Hello World"} 

## Termonology
- Path refers to the last part of the URL starting from the first '/'

So, in a URL like: \
https://example.com/items/foo \
...the path would be: \
/items/foo 

A "path" is also commonly called an "endpoint" or a "route". \
While building an API, the "path" is the main way to separate "concerns" and "resources".

- "Operation"  refers to one of the HTTP "methods":

In the HTTP protocol, you can communicate to each path using one (or more) of these "methods". \
When building APIs, you normally use these specific HTTP methods to perform a specific action.

POST: to create data
GET: to read data
PUT: to update data
DELETE: to delete data




