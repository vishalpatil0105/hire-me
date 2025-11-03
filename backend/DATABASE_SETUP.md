# Database Setup Guide

This guide explains how to set up the PostgreSQL database connection for the backend.

## AWS RDS PostgreSQL Configuration

The backend is configured to connect to an AWS RDS PostgreSQL database with the following settings:

- **Host**: `database-1.c9i0kwo087x1.eu-west-1.rds.amazonaws.com`
- **Port**: `5432`
- **Database Name**: `postgres`

## Environment Variables

Create a `.env` file in the `backend` directory with the following variables:

```env
DATABASE_HOST=database-1.c9i0kwo087x1.eu-west-1.rds.amazonaws.com
DATABASE_PORT=5432
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASSWORD=your_actual_password_here
```

**Important**: 
- Replace `your_actual_password_here` with your actual RDS database password
- Make sure your `.env` file is in `.gitignore` to keep credentials secure
- Never commit `.env` files to version control

## Installation Steps

1. **Install dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Create `.env` file**:
   Copy `.env.example` to `.env` and fill in your database credentials:
   ```bash
   cp .env.example .env
   # Then edit .env with your actual password
   ```

3. **Initialize database tables**:
   ```bash
   python init_db.py
   ```
   This will create the `users` and `jobs` tables in your PostgreSQL database.

4. **Run the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

## Database Tables

The application creates two main tables:

### Users Table
- `id` (Primary Key)
- `username` (Unique, Indexed)
- `email` (Unique, Indexed)
- `password_hash` (Bcrypt hashed password)

### Jobs Table
- `id` (Primary Key)
- `title` (Indexed)
- `description`
- `company`
- `location`

## Testing the Connection

You can test the database connection by checking the health endpoint:

```bash
curl http://localhost:8000/health
```

And verify the API is working:

```bash
curl http://localhost:8000/
```

## Troubleshooting

1. **Connection errors**: 
   - Verify your RDS security group allows connections from your IP
   - Check that the database credentials are correct
   - Ensure the database is running and accessible

2. **Table creation errors**:
   - Make sure you have proper permissions on the database
   - Check that the database exists and is accessible

3. **Import errors**:
   - Verify all requirements are installed: `pip install -r requirements.txt`
   - Make sure you're using Python 3.8 or higher


