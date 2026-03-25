from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}





@app.get("/teste12")
async def funcaoteste():
    return {"teste": "Deu Certo"}