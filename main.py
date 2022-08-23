# from unittest import result
from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki, wiki as wikilogic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """retreive wikipedia page"""

    answer = wikilogic(name)
    return {"result": answer}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """retreive wikipedia page and return phrases"""

    answer = wikilogic(name)
    return {"result": [answer]}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
