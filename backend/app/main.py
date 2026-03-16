from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #Basically used for connecting 2 diff ports
from dotenv import load_dotenv 
import os


load_dotenv() #Reads values in .env file and makes it known to entire app

#FastAPI instance
app = FastAPI(
    title = "DreamFinder API",
    version = "1.0.0"
)

#Basically using CORSMiddleware to allow communication between two diff ports
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

#GET REQUESTS
@app.get("/")
def root():
    return {"message" : "DreamFinder is Running."}

@app.get("/health")
def health():
    return {"Status" : "Healthy"}

@app.get("/trial")
def trial():
    return {"Trial" : "Success"}