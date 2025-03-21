"""
created via the following YOUTUBE tutorials & a crash reading of creating python classes
//https://www.youtube.com/watch?v=7vVKBRjFbeg
https://www.youtube.com/watch?v=C-bie4ZY_o0
used to test competency of creating API's and leveraging them in python over the course of 1 coding Binge
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
