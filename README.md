# News-Management

Overview
This Django-based News Management System allows administrators to efficiently create, edit, and organize news articles and categories through a secure web interface. Built for assignment submission at Melbourne Polytechnic, it demonstrates core concepts in web application development, relational data modeling, and the use of Django's built-in Admin tools.​

Features
Display of recent news articles on the public home page

Browse news articles by category

Full detail view for individual articles

Secure admin site for CRUD (Create, Read, Update, Delete) operations

Built-in user authentication for admin users

Robust data validation and model design

Technologies
Backend: Python, Django

Frontend: Django Templates, HTML, CSS

Database: SQLite (default Django setup)

Project Structure
text
Kim1525783_A3/
├── Kim1525783_A3/           # Django project config (settings, urls, wsgi, asgi)
├── news_management/         # Main Django app (models, views, forms, templates)
│   ├── migrations/
│   ├── templates/
│   │   └── news_management/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── article_detail.html
│   │       ├── categories.html
│   │       ├── category_detail.html
│   │       ├── news_form.html
│   │       ├── news_confirm_delete.html
│   │       └── registration/
│   │           └── login.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── tests.py
├── db.sqlite3               # SQLite database
├── manage.py
└── requirements.txt
Setup & Running Locally
Clone the repository:

text
git clone https://github.com/KimSuor23/News-Management-.git
cd News-Management-
(Optional but recommended) Create and activate a virtual environment:

text
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
Install dependencies:

text
pip install -r requirements.txt
Apply migrations:

text
python manage.py migrate
Create a superuser for admin access:

text
python manage.py createsuperuser
Run the development server:

text
python manage.py runserver
Access the app:

Open http://localhost:8000/ for the frontend

Open http://localhost:8000/admin for the Django Admin console

Main Functionalities
Public Frontend:

View recent news on the home page (latest 4 by publish date)

Browse all categories and filter articles by category

View full article details

Admin Console:

Login required for all management actions

Add, edit, and delete articles and categories using Django Admin

Validation: unique category names, non-empty news titles, data type checks

Sample Data Model
News: Title, Category (foreign key), Source, Published Date, Content

Category: Unique name per category

Acknowledgements
Developed as part of the Bachelor of IT (Software Development) – Melbourne Polytechnic, 2025.

Author
Kim Sour Liv
Bachelor of IT (Software Development)
Melbourne Polytechnic
