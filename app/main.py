from fastapi import FastAPI, Request, Response , File, Form, UploadFile
from starlette.middleware.cors import CORSMiddleware

from utils import config

from fastapi.testclient import TestClient

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/mocklogin")
async def mocklogin(request: Request, response:Response):
    try:
        body = await request.json()
        username = body['username']
        paswd = body['password']
        return{"msg":"succesfully logged in", "data":{"username":username, "password": paswd }}
    except Exception as e:
        response.status_code = config.HTTP_BAD_REQUEST400
        return{"msg":str(e), "data":[]}
@app.post("/file")
async def post_file(response:Response , email:str = Form() , file:UploadFile=File()):
    try:
        return{"msg":"success" , "data": []}
    except Exception as e:
        response.status_code = config.HTTP_BAD_REQUEST400
        return{"msg": str(e) , "data": []}

@app.get("/health_check")
async def read_main():
    return {"msg": " "}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": " "}
    return{"msg":" ","data": []}