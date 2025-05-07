from fastapi import FastAPI #importing api

app = FastAPI() #instatiate app


@app.get("/")
def root():
    return{"Message":"Hello sajan you are building api"}


"""OutPut:
        {"Message":"Hello sajan you are building api"}"""
