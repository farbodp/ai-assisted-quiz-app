from sqlalchemy.orm import Session

from schemas.quiz import QuizCreate
from models.models import Quiz, Question, Option
from dummy_data import dummy

def create_dummy_quiz(db: Session, quiz: QuizCreate):
    quiz = Quiz(
        name=quiz.name,
    )
    db.add(quiz)
    # Add some questions to the quiz
    question1 = Question(text="What is the result of 2 + 2?", quiz=quiz)
    db.add(question1)

    # Add some choices to the question
    choice1 = Option(text="1", correct=0, question=question1)
    choice2 = Option(text="2", correct=0, question=question1)
    choice3 = Option(text="3", correct=0, question=question1)
    choice4 = Option(text="4", correct=1, question=question1)
    db.add_all([choice1, choice2, choice3, choice4])

    question2 = Question(text="What is the result of 3 * 5?", quiz=quiz)
    db.add(question2)

    choice5 = Option(text="8", correct=0, question=question2)
    choice6 = Option(text="10", correct=1, question=question2)
    choice7 = Option(text="15", correct=0, question=question2)
    choice8 = Option(text="20", correct=0, question=question2)
    db.add_all([choice5, choice6, choice7, choice8])
    
    db.commit()
    db.refresh(quiz)
    return quiz