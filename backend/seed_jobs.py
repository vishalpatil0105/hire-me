"""
Script to seed the database with sample jobs
"""
from app.db.database import SessionLocal
from app.models.job import Job

def seed_jobs():
    db = SessionLocal()
    try:
        # Check if jobs already exist
        existing_jobs = db.query(Job).count()
        if existing_jobs > 0:
            print(f"Database already has {existing_jobs} jobs. Skipping seed.")
            return
        
        # Sample jobs data
        sample_jobs = [
            {
                "title": "Senior Software Engineer",
                "description": "We are looking for an experienced software engineer to join our team. You will be responsible for designing and developing scalable web applications using modern technologies.",
                "company": "Tech Innovations Inc.",
                "location": "San Francisco, CA"
            },
            {
                "title": "Data Scientist",
                "description": "Join our data science team to build predictive models and analyze large datasets. Experience with machine learning and Python required.",
                "company": "Data Analytics Corp",
                "location": "New York, NY"
            },
            {
                "title": "Product Manager",
                "description": "Lead product development and strategy for our SaaS platform. Work closely with engineering, design, and marketing teams to deliver exceptional products.",
                "company": "Cloud Solutions Ltd",
                "location": "Austin, TX"
            },
            {
                "title": "Frontend Developer",
                "description": "Create beautiful and responsive user interfaces using React, TypeScript, and modern CSS. Collaborate with designers to implement pixel-perfect designs.",
                "company": "Digital Creations",
                "location": "Seattle, WA"
            },
            {
                "title": "Backend Developer",
                "description": "Build robust and scalable backend systems using Python, FastAPI, and PostgreSQL. Experience with REST APIs and database design required.",
                "company": "API Masters",
                "location": "Boston, MA"
            },
            {
                "title": "DevOps Engineer",
                "description": "Manage cloud infrastructure, CI/CD pipelines, and deployment automation. Experience with AWS, Docker, and Kubernetes preferred.",
                "company": "Infrastructure Solutions",
                "location": "Denver, CO"
            },
            {
                "title": "Full Stack Developer",
                "description": "Work on both frontend and backend development. Build end-to-end features from database design to user interface implementation.",
                "company": "Full Stack Innovations",
                "location": "Remote"
            },
            {
                "title": "UI/UX Designer",
                "description": "Design intuitive and engaging user experiences. Create wireframes, prototypes, and high-fidelity designs using Figma or Sketch.",
                "company": "Design Studio Pro",
                "location": "Los Angeles, CA"
            }
        ]
        
        print("Seeding database with sample jobs...")
        for job_data in sample_jobs:
            job = Job(**job_data)
            db.add(job)
        
        db.commit()
        print(f"Successfully added {len(sample_jobs)} jobs to the database!")
        
        # Verify
        total_jobs = db.query(Job).count()
        print(f"Total jobs in database: {total_jobs}")
        
    except Exception as e:
        print(f"Error seeding jobs: {e}")
        db.rollback()
        import traceback
        traceback.print_exc()
    finally:
        db.close()

if __name__ == "__main__":
    seed_jobs()

