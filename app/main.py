from fastapi import FastAPI

from app.database.models import init_db
from app.routers.problems import router

app = FastAPI(title="DSA Revision Scheduler")

init_db()

app.include_router(router)


@app.get("/")
def home():
    return {"message": "DSA Revision Scheduler API Running"}