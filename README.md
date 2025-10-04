# Library Shelf Token Management System

A Django-based backend system for managing library shelf assignments and retrievals securely using token-based confirmations and dual user-admin approvals.

---

## Description

This system helps streamline the manual process of bag management in libraries by assigning shelves to students with unique tokens and requiring admin approval for assignments and retrievals. The workflow guarantees secure shelf usage, prevents mix-ups, and provides a clear admin panel for approvals.

---

## Features

- Immediate shelf assignment request with unique shelf number and token shown to student.
- Admin approval required to finalize shelf assignment.
- Students can request retrieval; admin confirms using shelf number and token.
- Simple dashboards for users (students) and admins.
- Status tracking with clear stages (requested, assigned, retrieval requested, collected).
- Secure token-based verification for shelf ownership.
- Admin messages for approvals and retrieval confirmations.
- No timing/duration tracking (simplified for ease of use).

---

## Users Included (Pre-configured for quick testing)

| Username | Password       | Role   |
| -------- | -------------- | ------ |
| lakshya  | mypassword123  | User   |
| john     | john123        | User   |
| admin    | admin          | Admin  |

(**Note:** Create these users manually via Django admin or using manage.py shell before testing.)

---

## Installation & Setup

1. **Clone the repository**

<pre>git clone https://github.com/Lakshya507/Library_Backend.git
cd Library_Backend</pre>

2. **Create and activate a virtual environment**

<pre>python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate</pre>

3. **Install dependencies**
<pre>pip install django</pre>


4. **Apply database migrations**

<pre>python manage.py makemigrations
python manage.py migrate</pre>


5. **Create users (if not already created)**

Use Django admin or shell commands to create:
<pre>python manage.py createsuperuser # For admin user</pre>

Or create users manually in shell You Can make like this:
<pre>python manage.py shell

from django.contrib.auth.models import User
User.objects.create_user('lakshya', password='mypassword123')
User.objects.create_user('john', password='john123')
User.objects.create_superuser('admin', password='admin')</pre>


6. **Run the development server**
<pre>python manage.py runserver</pre>


7. **Access**

- User dashboard: `http://localhost:8000/index/`
- Admin dashboard: `http://localhost:8000/admin_shelves/`

---

## Usage

- Students log in to assign shelves and see their unique shelf number and token.
- Admins log in to approve shelf assignments and confirm retrievals.
- The system ensures secure mutual confirmation for shelf use.
- Users receive only their own notification messages; assignment messages appear on the admin side.

---

## Project Structure Overview
<pre>
Library_Backend/
│
├── home/
│   ├── migrations/
│   ├── __init__.py                 # empty file
│   ├── admin.py                   # (default or your admin config)
│   ├── apps.py                   # app configuration
│   ├── models.py                 # ShelfToken model
│   ├── views.py                  # User and admin views 
│   ├── urls.py                   # URL routing for app
│   ├── templates/
│   │   ├── index.html            # User dashboard template
│   │   └── admin_shelves.html   # Admin dashboard template
│   └── templatetags/             
│
├── Library_Backend/                 # Django project folder
│   ├── __init__.py              # empty file
│   ├── settings.py              # project settings
│   ├── urls.py                  # project-level urls.py
│   └── wsgi.py                  # project WSGI config
│
└── manage.py                    # Django management command entrypoints
</pre>



---

## License

Developed by Lakshyaraj Mandloi. Licensed under MIT License.

---


