import faiss
from sentence_transformers import SentenceTransformer
# from pypdf import PdfReader
import numpy as np
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml
from fastapi import FastAPI
import asyncio

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

@app.post("/query?{prompt}")
def post_item(prompt: str):
    retrieve_chunks
    await llm response
    return response

