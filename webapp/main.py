import os
import base64
from typing import Union
from os.path import dirname, abspath, join
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import hashlib

current_dir = dirname(abspath(__file__))
static_path = join(current_dir, "static")

app = FastAPI()
app.mount("/ui", StaticFiles(directory=static_path), name="ui")


class Body(BaseModel):
    length: Union[int, None] = 20


@app.get('/')
def root():
    html_path = join(static_path, "index.html")
    return FileResponse(html_path)


@app.post('/generate')
def generate(body: Body):
    """
    Generate a pseudo-random token ID of twenty characters
    by default.
    Example POST request body:
    {
        "length": 20
    }
    """
    string = base64.b64encode(os.urandom(64))[:body.length].decode('utf-8')
    return {'token': string}


"""
Class code provided when doing excercise

"""


class Text(BaseModel):
    text: str


"""
Generated code by Copilote lines === post/checksum
"""


@app.post('/checksum')
def checksum(text: Text):
    """
    Calculate the checksum of the provided text. Example POST request body:

    {
        "text": "example text"
    }
    """
    checksum_value = hashlib.md5(text.text.encode('utf-8')).hexdigest()
    return {'checksum': checksum_value}
