from fastapi import FastAPI

app = FastAPI()

@app.get("/say_hi")
async def root():
    return {"msg": "Hello World", "data": []}
