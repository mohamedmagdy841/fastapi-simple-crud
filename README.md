# FastAPI CRUD

A modern articles platform built with FastAPI, SQLite, and other technologies.

## Features

- User authentication (Sign Up, Login, JWT)
- Article management (CRUD)
- Email notifications (using Jinja2 templates)
- Password reset (via email with token)

## Requirements

- Python 3.8+
- FastAPI, SQLAlchemy, Alembic
- SQLite (local development)

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/mohamedmagdy841/fastapi-blog.git
   cd fastapi-blog
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in `.env` (see `.env.example` for details).

5. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

## Database Migrations

1. Create migrations:
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```

2. Apply migrations:
   ```bash
   alembic upgrade head
