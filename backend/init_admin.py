"""
Initialize admin user in the database
"""
from app.db.database import SessionLocal
from app.models.user import User
from app.core.config import get_password_hash, settings

def init_admin():
    db = SessionLocal()
    try:
        # Check if admin already exists
        admin = db.query(User).filter(User.email == settings.ADMIN_EMAIL).first()
        
        if admin:
            print(f"Admin user already exists: {settings.ADMIN_EMAIL}")
            # Update to ensure it's an admin
            admin.is_admin = True
            admin.password_hash = get_password_hash(settings.ADMIN_PASSWORD)
            db.commit()
            print("Admin user updated successfully!")
        else:
            # Create admin user
            admin_user = User(
                email=settings.ADMIN_EMAIL,
                username="admin",
                password_hash=get_password_hash(settings.ADMIN_PASSWORD),
                is_admin=True
            )
            db.add(admin_user)
            db.commit()
            print(f"Admin user created successfully!")
            print(f"Email: {settings.ADMIN_EMAIL}")
            print(f"Password: {settings.ADMIN_PASSWORD}")
        
    except Exception as e:
        print(f"Error creating admin: {e}")
        db.rollback()
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    init_admin()


