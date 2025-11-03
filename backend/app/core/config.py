import os
import bcrypt
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database settings - defaults to AWS RDS endpoint you provided
    DATABASE_HOST: str = os.getenv("DATABASE_HOST", "database-1.c9i0kwo087x1.eu-west-1.rds.amazonaws.com")
    DATABASE_PORT: str = os.getenv("DATABASE_PORT", "5432")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "postgres")
    DATABASE_USER: str = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD: str = os.getenv("DATABASE_PASSWORD", "")
    
    # Admin credentials
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "admin@jobsearch.com")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "admin123")
    
    @property
    def DATABASE_URL(self) -> str:
        """Construct PostgreSQL connection URL"""
        return f"postgresql+psycopg2://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"  # Ignore extra fields in .env file

settings = Settings()

# Password hashing functions using bcrypt directly
def get_password_hash(password: str) -> str:
    """Hash a password using bcrypt"""
    # Convert password to bytes
    password_bytes = password.encode('utf-8')
    # Truncate to 72 bytes if needed (bcrypt limit)
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    # Generate salt and hash
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    # Return as string (bcrypt hash is a bytes object)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash.
    
    Handles both bcrypt hashes (new passwords) and plain text (old passwords for backward compatibility).
    """
    if not hashed_password:
        return False
    
    try:
        # Check if the stored password is a bcrypt hash (starts with $2b$, $2a$, or $2y$)
        if hashed_password.startswith(('$2b$', '$2a$', '$2y$')):
            # It's a bcrypt hash, verify normally
            password_bytes = plain_password.encode('utf-8')
            if len(password_bytes) > 72:
                password_bytes = password_bytes[:72]
            hashed_bytes = hashed_password.encode('utf-8')
            return bcrypt.checkpw(password_bytes, hashed_bytes)
        else:
            # It's plain text (old password), do simple comparison
            # Note: This is for backward compatibility only
            return plain_password == hashed_password
    except Exception as e:
        # Log the error for debugging
        import logging
        logging.error(f"Password verification error: {e}")
        return False
