from fastapi import FastAPI
import uvicorn
from database import SessionLocal, engine, Base
from routers import user

Base.metadata.create_all(bind = engine)

app = FastAPI(title = "Storage API")

app.include_router(user.router, prefix='/user')

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
