from fastapi import FastAPI

app = FastAPI()

# The @app.get("/") tells FastAPI that the function right below is in charge of handling requests that go to:
# the path /
# using a get operation
@app.get("/")
async def root():
    return {"message": "Hello World"}