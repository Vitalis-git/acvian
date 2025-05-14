from fastapi import FastAPI
import uvicorn 
import requests

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test")
def fetch_html(url: str) -> str:
    url = "http://" + url
    response = requests.get(url)
    response.raise_for_status()
    return response.text
