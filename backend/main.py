from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from db.session import engine
from models.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    return """
        <html>
            <head>
                <title>FastAPI App</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
            </body>
        </html>
    """

