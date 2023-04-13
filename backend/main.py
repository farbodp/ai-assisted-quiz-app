from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session


from db.session import SessionLocal
from db.session import engine
from models.models import Base
from schemas.quiz import QuizCreate
from crud.quiz import create_dummy_quiz

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/quizes/")
def post_dummy_quiz(quiz: QuizCreate, db: Session = Depends(get_db)):
    dummy_quiz = create_dummy_quiz(
        db = db,
        quiz = quiz
    )
    return dummy_quiz


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

