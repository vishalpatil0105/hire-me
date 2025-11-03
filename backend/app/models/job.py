from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False, index=True)
    description = Column(Text, nullable=False)
    company = Column(String(200), nullable=False)
    location = Column(String(200), nullable=True)
