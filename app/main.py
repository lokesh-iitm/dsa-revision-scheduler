from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.database.models import init_db
from app.routers.problems import router as problem_router
from app.routers.revisions import router as revision_router

app = FastAPI(title="DSA Revision Scheduler")

init_db()

app.include_router(problem_router)
app.include_router(revision_router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html"
    )