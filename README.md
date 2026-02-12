# Portfolio Project

A professional portfolio website built with Django and Tailwind CSS.

## Setup Instructions

1.  **Clone the repository** (if not already local).
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Environment Variables**:
    - Copy `.env.example` to `.env`.
    - Update `SECRET_KEY` and other settings if deploying.
5.  **Database Migration**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6.  **Create Superuser** (for Admin Panel):
    ```bash
    python manage.py createsuperuser
    ```
7.  **Run Development Server**:
    ```bash
    python manage.py runserver
    ```
8.  **Access Admin Panel**:
    - Go to `http://127.0.0.1:8000/admin/`
    - Log in and add Projects, Skills, Certifications.

## Deployment (Render/Heroku)

This project is configured for deployment with `gunicorn`, `whitenoise`, and `dj-database-url`.

1.  Push code to GitHub.
2.  Connect repository to your hosting provider (Render/Heroku).
3.  Set Environment Variables in the dashboard (`SECRET_KEY`, `DATABASE_URL` is usually auto-set by postgres addon, `DEBUG=False`).
4.  Build command: `pip install -r requirements.txt && python manage.py migrate`.
5.  Start command: `gunicorn portfolio.wsgi`.
