"""
//api.py
//https://www.youtube.com/watch?v=7vVKBRjFbeg
"""
from fastapi import FastAPI

#from services.hello_service import Greeting

app = FastAPI()

class Greetings:
    def __init__(self, h, g):
        self.say_hello = h
        self.say_goodbye =  g
greeting = Greetings("yo", "cya")

@app.get("/")
def root():
        return {"hello": "worldi"}

@app.get("/helo")
async def say_hello():
      #  Greeting = Greetings()
        return {"Outro": greeting.say_hello}

@app.get("/goodbyte")
def root():
   #     Greeting = Greetings()
        return {"Outro": greeting.say_goodbye}
@app.get("/hello")
def root():  
        return {"message": greeting.say_hello}

@app.get("/goodbye")
async def say_goodbye():
     #   Greeting = Greetings()
        return {"message": greeting.say_goodbye}