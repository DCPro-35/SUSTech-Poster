from __future__ import annotations
import argparse
import asyncio
import os
import random
import sys
import uuid
from enum import Enum
from typing import Generator
from typing import Literal
from typing import Optional
from typing import Union
import numpy as np
import requests
import websockets.client as websockets
import datetime
from prompt import *
import EdgeGPT
from  EdgeGPT import Chatbot

COOKIE = "../data/cookie/cookie.json"
TRAIN_PATH = "../data/input/Data.txt"
TEST_PATH = "../data/input/Label.txt"
OUTPUT_PATH = "../data/output/"
PROXY = "http://127.0.0.1:1080"

#invoke a chat of keyword extraction
async def keyword_extract(bot):
    wrote = 0
    
    prompt = generate_prompt()
    return_msg = ""
    async for final, response in bot.ask_stream(
        prompt=prompt,
        conversation_style="balanced",
    ):
        
        if not final:
            print(response[wrote:], end="")
            #concat the string with the message
            return_msg = return_msg + response[wrote:]
            wrote = len(response)
            sys.stdout.flush()
        
        else:
            return return_msg.strip()

#invoke a chat of normal conversation
async def normal_chat(bot):
    wrote = 0
    reply = ""
    prompt = "你好"
    return_msg = ""
    async for final, response in bot.ask_stream(
        prompt=prompt,
        conversation_style="balanced",
    ): 
        if not final:
            print(response[wrote:], end="")
            #concat the string with the message
            return_msg = return_msg + response[wrote:]
            wrote = len(response)
            sys.stdout.flush()
        
        else:
            reply=return_msg.strip()
    
    return reply

#edit the response to json format
def to_json(response):
    #select the string between the first "[" and the last "]", 

    response = response[response.find("["):response.rfind("]")+1]
    #write the response to a json file
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    out = OUTPUT_PATH +current_time+ "response.json"
    with open(out, "w") as f:
        f.write(response)
        f.close()

async def main():

    print("\nLoading cookie from: " + COOKIE)
    print()
    
    # sys.exit()
    X_test = np.loadtxt(TEST_PATH, dtype=str, delimiter="\t")
    X_train = np.loadtxt(TRAIN_PATH, dtype=str, delimiter="\t")

    #initialize the bot
    bot = Chatbot(cookiePath = COOKIE)
    
    response = await keyword_extract(bot)
    await bot.close()
    #save the response to the file and rename it accroding to time
    
    to_json(response)
    
    # current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
    # out_file = OUTPUT_PATH + current_time + ".txt"
    # # create a file named out_file

    # with open(out_file, "a") as f:
    #     f.write(response + "\n")
    #     f.close()

    print("Done")

if __name__ == "__main__":
    asyncio.run(main())
