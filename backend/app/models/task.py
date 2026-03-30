from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship

from app.db.session import Base


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(String(255), nullable=False)

    # Admin who created this task
    created_by = Column(Integer, ForeignKey('users.id'))

    creator = relationship('User', back_populates='created_tasks')
