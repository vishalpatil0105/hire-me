from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
import logging
from app.db.database import get_db
from app.models.user import User
from app.schemas.auth import UserCreate, UserOut, UserLogin
from app.core.config import get_password_hash, verify_password

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Check if email already exists
        db_user = db.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Check if username already exists
        db_user = db.query(User).filter(User.username == user.username).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username already taken")
        
        # Create new user with hashed password
        logger.info(f"Creating user with email: {user.email}, username: {user.username}")
        
        try:
            password_hash = get_password_hash(user.password)
            logger.info(f"Password hashed successfully, hash length: {len(password_hash)}")
            
            new_user = User(
                email=user.email,
                username=user.username,
                password_hash=password_hash,
                is_admin=False
            )
            logger.info(f"User object created")
            
            db.add(new_user)
            logger.info(f"User added to session")
            
            db.flush()  # Flush to get ID before commit
            logger.info(f"User flushed, ID: {new_user.id}")
            
            db.commit()
            logger.info(f"User committed to database successfully")
            
            db.refresh(new_user)
            logger.info(f"User refreshed, final ID: {new_user.id}")
            
            return new_user
        except Exception as e:
            logger.error(f"Error during user creation: {e}", exc_info=True)
            db.rollback()
            raise
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except OperationalError as e:
        logger.error(f"Database connection error: {e}")
        raise HTTPException(
            status_code=503,
            detail="Database connection failed. Please check your database configuration and ensure tables are created."
        )
    except SQLAlchemyError as e:
        logger.error(f"Database error during signup: {e}")
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error occurred: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error during signup: {e}", exc_info=True)
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )

@router.post("/login", response_model=UserOut)
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        logger.info(f"Login attempt for email: {user.email}")
        # Check if user exists with the given email
        db_user = db.query(User).filter(User.email == user.email).first()
        
        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        # Get password hash from database and verify the provided password
        if not verify_password(user.password, db_user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid email or password")
        
        # Password matches, return user
        return db_user
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except OperationalError as e:
        logger.error(f"Database connection error: {e}")
        raise HTTPException(
            status_code=503,
            detail="Database connection failed. Please check your database configuration."
        )
    except SQLAlchemyError as e:
        logger.error(f"Database error during login: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Database error occurred: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Unexpected error during login: {e}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )
