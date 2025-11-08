# News-Management

📰 News Management Web App

A Django web application project developed for Melbourne Polytechnic. Admins can easily manage news articles and categories through a secure, responsive interface.

🚀 Features
🛡️ Admin Features:

- Add, edit, and delete news articles

- Organize articles into categories

- Admin login for management access

- Validate unique categories and non-empty fields

🌎 Public Features:

- Browse news by category

- View latest news articles on the homepage

- See full details of individual articles

🛠️ Technologies Used
- Backend: Python, Django

- Frontend: Django Templates, HTML, CSS

- Database: SQLite (default)

📝 How to Run
Clone this repository

1. text run
   git clone https://github.com/KimSuor23/News-Management-.git

  - Install Django (if not installed)

2. text
  pip install django

  - Run database migrations

3. text
  python manage.py migrate

  - Create admin account

4. text
  python manage.py createsuperuser

  - Start the development server

5. text
  python manage.py runserver

  - View site: http://localhost:8000/

  - Django Admin: http://localhost:8000/admin

📁 Project Structure
Kim1525783_A3/ – Django project settings (settings.py, urls.py, asgi.py, wsgi.py)

news_management/ – App code and templates

db.sqlite3 – Database file

👤 Author
Kim Sour Liv
Bachelor of IT (Software Development)
Melbourne Polytechnic
