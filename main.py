from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import func


# App Config

app = FastAPI()
Base = declarative_base() 

app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")






## App Model

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True),
    title = Column(String)
    content = Column(String)
    created_at = Column(String, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def _str__(self):
        return self.title

## App Routes

@app.get('/')
async def index(request : Request):
    return templates.TemplateResponse(request, "base.html", {})


