from pydantic import BaseModel
from typing import List, Optional

class JobBase(BaseModel):
    title: str
    description: str
    company: str
    location: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    id: int

    class Config:
        from_attributes = True

class JobListResponse(BaseModel):
    jobs: List[JobOut]
