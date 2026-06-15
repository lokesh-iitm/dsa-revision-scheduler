from fastapi import FastAPI

from app.database.models import init_db
from app.routers.problems import router as problem_router
from app.routers.revisions import router as revision_router

app = FastAPI(title="DSA Revision Scheduler")

init_db()

app.include_router(problem_router)
app.include_router(revision_router)


@app.get("/")
def home():
    return {"message": "DSA Revision Scheduler API Running"}