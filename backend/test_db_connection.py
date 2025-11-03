"""
Quick script to test database connection and create tables if needed.
"""
import sys
from app.db.database import engine, Base
from app.models import user, job
from app.core.config import settings

def test_connection():
    """Test database connection and create tables"""
    print("Testing database connection...")
    print(f"Host: {settings.DATABASE_HOST}")
    print(f"Port: {settings.DATABASE_PORT}")
    print(f"Database: {settings.DATABASE_NAME}")
    print(f"User: {settings.DATABASE_USER}")
    print(f"Password: {'*' * len(settings.DATABASE_PASSWORD) if settings.DATABASE_PASSWORD else '(empty)'}")
    print()
    
    try:
        # Test connection
        with engine.connect() as conn:
            print("[OK] Database connection successful!")
        
        # Create tables
        print("\nCreating/verifying database tables...")
        Base.metadata.create_all(bind=engine)
        print("[OK] Tables created/verified successfully!")
        
        # List tables
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print(f"\nTables in database: {tables}")
        
        return True
    except Exception as e:
        print(f"\n[ERROR] {e}")
        print("\nTroubleshooting:")
        print("1. Check if DATABASE_PASSWORD is set in .env file")
        print("2. Verify RDS security group allows connections from your IP")
        print("3. Ensure the database is running and accessible")
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)

