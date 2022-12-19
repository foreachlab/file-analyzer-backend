from fastapi import FastAPI

app = FastAPI()

@app.get("/say_hi")
async def root():
    return {"msg": "Hello World", "data": []}

@app.get("/profile/{profile_id}")  
async def get_profile_id(profile_id: int):
    return { "msg": "" , "data": {"profile_id": profile_id}}

@app.get("/component/")
async def read_component(number: int, text: str):
    number+= 1
    return{"msg": "" , "data":{"number": number , "text" : text}}
