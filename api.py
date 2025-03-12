from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/user/{username}/{age}")
async def login(username: str = Path(min_length=3, max_length=15, description='Enter your username', example='Ilya'),
                age: int = Path(ge=0, le=100, description="Enter your age")) -> dict:
    return {"user": username, "age": age}