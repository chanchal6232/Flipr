Digital Agency - Full Stack Django Project
🚀 Quick Start Guide
Prerequisites
Python 3.8 or higher

Git (optional)

Installation Steps
Clone or Download the Project

bash
https://github.com/chanchal6232/Flipr
cd Flipr
Create Virtual Environment

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install Dependencies

bash
pip install -r requirements.txt
Setup Database

bash
python manage.py migrate
Create Admin User

bash
python manage.py createsuperuser
# Follow prompts to create username, email, password
Add Sample Data (Optional)

bash
python sample_data.py
Run Development Server

bash
python manage.py runserver
🌐 Access the Application
Once server is running, open your browser:

Homepage: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/dashboard/

Django Admin: http://127.0.0.1:8000/admin/ (login with superuser)

📁 Project Structure
text
digital-agency/
├── main/                    # Main application
├── admin_panel/            # Admin dashboard
├── templates/              # HTML templates
├── static/                 # CSS, JS files
├── media/                  # Uploaded images
├── requirements.txt        # Python packages
├── manage.py              # Django command tool
└── README.md              # This file

🎯 Features Implemented
Landing Page
Projects showcase with images and descriptions

Client testimonials section

Contact form with validation

Newsletter subscription

Admin Panel
Dashboard with statistics

Add/edit/delete projects

Manage client testimonials

View contact form submissions

View newsletter subscribers

Technical Features
Image upload with auto-cropping

REST API for form submissions

Responsive Bootstrap design

SQLite database

🔧 Troubleshooting
Common Issues
Port already in use

bash
python manage.py runserver 8001
Module not found errors

bash
pip install -r requirements.txt
Database errors

bash
python manage.py migrate
Static files not loading

bash
python manage.py collectstatic
For Development
Set DEBUG = True in settings.py

Use db.sqlite3 for local database

Images uploaded to media/ folder

📞 Need Help?
If you face any issues while running the project, check:

Python version (should be 3.8+)

All dependencies installed

Database migrated

Server is running

