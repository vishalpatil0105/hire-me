"""
Script to check if users are in the database
"""
from app.db.database import SessionLocal
from app.models.user import User

def check_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        print(f"\nTotal users in database: {len(users)}")
        for user in users:
            print(f"  - ID: {user.id}, Email: {user.email}, Username: {user.username}")
        if len(users) == 0:
            print("\n[INFO] No users found in database")
    except Exception as e:
        print(f"\n[ERROR] {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_users()

