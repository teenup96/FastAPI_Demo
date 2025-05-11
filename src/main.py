
from fastapi import FastAPI, HTTPException
# Python

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/{num1}/{num2}")
async def read_item(num1: int, num2: int):
    sum_num = num1 + num2
    return {"sum": sum_num}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)