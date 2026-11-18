
# Student Course API

A simple backend API for a university student portal.

## Technology
- Python
- Flask
- Flask-CORS
- Gunicorn

## API Endpoints

| Method | Endpoint | Description |
| GET | /api/health | Check API status |
| GET | /api/courses | Get all courses |
| GET | /api/courses/1 | Get one course |
| GET | /api/courses/9999 | Test invalid course |

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start the application:

python app.py

## Render Deployment

Build command:

pip install -r requirements.txt

Start command:

gunicorn app:app

## Database

This prototype uses fictional sample data.
It does not connect to a database.
