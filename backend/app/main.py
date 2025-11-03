from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import auth, jobs
from app.db.database import Base, engine
from app.models import user, job
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create database tables (only if connection is available)
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created/verified successfully")
except Exception as e:
    logger.warning(f"Could not create database tables on startup: {e}")
    logger.info("Tables will be created when first connection is made, or run 'python init_db.py'")

app = FastAPI(
    title="Job Search API",
    description="A job search application API",
    version="1.0.0"
)

# CORS configuration - allow requests from React frontend
# Get allowed origins from environment variable or use defaults
import os
cors_origins = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else []
# Add default localhost origins for development
default_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
# Combine and filter empty strings
allowed_origins = [origin.strip() for origin in cors_origins + default_origins if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(auth.router)
app.include_router(jobs.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Search API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
