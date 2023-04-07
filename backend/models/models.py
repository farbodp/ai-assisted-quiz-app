from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from db.session import Base

class Quiz(Base):
    __tablename__ = "quizes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    questions = relationship("Question", back_populates="quiz")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    quiz_id = Column(Integer, ForeignKey("quizes.id"))
    quiz = relationship("Quiz", back_populates="questions")
    options = relationship("Option", back_populates="question")

class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
    question = relationship("Question", back_populates="options")
