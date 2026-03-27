from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "Hello, Welcome to FastAPI!"}


@app.middleware("http")
async def log_requests(request: Request, call_next):

    print("Before request")
    print("Method:", request.method)
    print("Path:", request.url.path)

    response = await call_next(request)

    print("After request")

    return response


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):

    return JSONResponse(
        status_code=404,
        content={
            "message": "The requested resource was not found"
        }
    )