from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/search")
def student_data (name: str = Query(None, description="Enter your name here"),
                  age: int = Query(None, description="Enter your age here")):
    
    return {"name": name, "age": age}