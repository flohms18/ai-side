from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware


# App Config

app = FastAPI()

app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/')
async def index(request : Request):
    return templates.TemplateResponse(request, "base.html", {})

