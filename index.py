#import fastapi
from fastapi import FastAPI
from routes.student import student_router
from fastapi.middleware.cors import CORSMiddleware

client_app =['http://localhost:3000']#our React app will be runing on this ip and port



#create app
app = FastAPI()
#register your router
app.include_router(student_router)
#Register App with Cors middlexware to allow resource sharing different domains/origin

app.add_middleware(
    CORSMiddleware,
    allow_origins=client_app,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)