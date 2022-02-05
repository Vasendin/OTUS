from typing import Optional
import uvicorn
import os
from fastapi import FastAPI, Body, HTTPException, status, Depends, Query


app = FastAPI(title="Ping pong")
print("RUN")

@app.get("/")
def read_root(
    q: Optional[str] = Query(None),
):
    return "Hello"


@app.get("/ping")
def ping():
    return {"message": "pong"}


# if __name__ == '__main__':
#     uvicorn.run(app, host="0.0.0.0", port=8080)
