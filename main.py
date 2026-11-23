from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# Import Models

import model



# App Config

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/',response_class=HTMLResponse)
async def home(request : Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

