from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .api import router
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Resume Parser Microservice")
app.include_router(router)

app.mount("/", StaticFiles(directory="app/static", html=True), name="static")