from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root(name: str = "sajan"):
    return {"message": f"Hello {name} you are in the right way"}

"""output:
{"message":"Hello sajan you are in the right way"}"""