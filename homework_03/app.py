from fastapi import FastAPI


app = FastAPI(title="Ping pong")
print("RUN")

@app.get("/")
def read_root():
    return "Hello"


@app.get("/ping")
def ping():
    return {"message": "pong"}
