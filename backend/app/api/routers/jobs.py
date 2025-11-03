from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.database import get_db
from app.models.job import Job
from app.models.user import User
from app.schemas.job import JobOut, JobCreate

router = APIRouter(prefix="/api/jobs", tags=["jobs"])

@router.get("", response_model=List[JobOut])
def get_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all jobs - accessible to everyone"""
    jobs = db.query(Job).offset(skip).limit(limit).all()
    return jobs

@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    """Get a specific job by ID - accessible to everyone"""
    job = db.query(Job).filter(Job.id == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("", response_model=JobOut)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    x_admin_email: Optional[str] = Header(None, alias="X-Admin-Email")
):
    """Create a new job - Admin only"""
    if not x_admin_email:
        raise HTTPException(status_code=403, detail="Admin authentication required")
    
    admin_user = db.query(User).filter(
        User.email == x_admin_email,
        User.is_admin == True
    ).first()
    
    if not admin_user:
        raise HTTPException(status_code=403, detail="Admin access required to create jobs")
    
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
