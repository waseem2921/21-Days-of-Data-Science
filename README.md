# 21 Days of Data Science

A modern Django portfolio app to showcase Day 1 to Day 21 Data Science and Analytics projects.

## Features

- Modern landing page with hero section and smooth scrolling
- Dynamic project dashboard (Day 1 to Day 21)
- Search and technology filter
- Detailed dynamic project pages via `/projects/day-<n>/`
- Admin-powered content management
- Animated stats section
- Light/Dark theme toggle
- Render-ready production setup

## Tech Stack

- Django
- HTML, CSS, Bootstrap
- JavaScript
- SQLite (local)
- PostgreSQL-ready via `DATABASE_URL`

## Local Setup

1. Create and activate your virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy env file and edit secrets:

   ```bash
   cp .env.example .env
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create admin user:

   ```bash
   python manage.py createsuperuser
   ```

6. Seed Day 1 to Day 21 projects:

   ```bash
   python manage.py seed_projects
   ```

7. Start server:

   ```bash
   python manage.py runserver
   ```

## Render Deployment

1. Push the project to GitHub.
2. In Render, create a new **Web Service** from your GitHub repo.
3. Render can auto-detect `render.yaml`, or you can manually set:
   - Build command: `./build.sh`
   - Start command: `gunicorn data_science.wsgi:application`
4. Add environment variables in Render:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=<your-render-domain>`
   - `DJANGO_CSRF_TRUSTED_ORIGINS=https://<your-render-domain>`
   - `DATABASE_URL` (from Render PostgreSQL or external DB)
5. Trigger deploy.

## Content Management

- Visit `/admin/`
- Add or edit projects in the **Project** model
- Technologies must be comma-separated (e.g., `Python, Pandas, SQL`)

## Production Notes

- `DEBUG=False` is controlled by env vars
- Whitenoise serves static files
- Gunicorn used for WSGI
- Postgres-ready through `dj-database-url`
- Media files are stored locally by default; use object storage for production scale
