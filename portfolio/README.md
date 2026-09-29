# DevOrbit Glassmorphism Portfolio

This package contains the portfolio UI rebuilt as a server-rendered Django project. The frontend uses semantic HTML, a Tailwind CSS CDN utility layer, and a custom stylesheet for the pastel glassmorphism design. Portfolio content is managed from Django Admin and stored in SQLite for quick local development or MySQL for Workbench-backed usage.

## Local setup

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, then create the database schema and administrator account:

```bash
python manage.py migrate

python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the portfolio and `http://127.0.0.1:8000/admin/` for content management.

## MySQL Workbench configuration

Create a database in MySQL Workbench, for example `devorbit`, and grant a local user access. Set `DB_ENGINE=mysql` and fill in the `MYSQL_*` variables in `.env`. Then run `python manage.py migrate`. The project keeps SQLite as the default so a new developer can preview the UI without installing MySQL first.

## Admin content workflow

Create one `SiteProfile` record, then add `Skill`, `Project`, `Experience`, and `SocialLink` records from the admin panel. Upload the portrait and project images through their image fields. Contact form submissions appear under `Contact messages`.

## Important notes

The supplied portrait is referenced in the original UI package, but this standalone archive expects you to upload your preferred portrait through Django Admin. The project is intentionally ready for real content rather than seeded fake testimonials or reviews. Tailwind is loaded from the CDN for easy setup; for an offline production build, replace it with a compiled Tailwind pipeline.
