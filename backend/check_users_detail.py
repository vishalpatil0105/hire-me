"""
Script to check users with more detail
"""
from app.db.database import SessionLocal
from app.models.user import User

def check_users_detail():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        print(f"\nTotal users in database: {len(users)}")
        print("\n" + "="*60)
        for user in users:
            print(f"ID: {user.id}")
            print(f"Email: {user.email}")
            print(f"Username: {user.username}")
            print(f"Password Hash: {user.password_hash[:50]}..." if user.password_hash else "No password hash")
            print("="*60)
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    check_users_detail()

