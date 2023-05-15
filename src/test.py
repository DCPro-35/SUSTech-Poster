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
from  EdgeGPT import Chatbot

COOKIE = "../data/cookie/cookie.json"
TRAIN_PATH = "../data/input/Data.txt"
TEST_PATH = "../data/input/Label.txt"
OUTPUT_PATH = "../data/output/"
PROXY = "http://127.0.0.1:1080"

