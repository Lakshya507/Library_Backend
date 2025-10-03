Library Shelf Token Management System
A Django-based backend system for managing library shelf assignments and retrievals securely using token-based confirmations and dual user-admin approvals.

Description
This system helps streamline the manual process of bag management in libraries by assigning shelves to students with unique tokens and requiring admin approval for assignments and retrievals. The workflow guarantees secure shelf usage, prevents mix-ups, and provides a clear admin panel for approvals.

Features
Immediate shelf assignment request with unique shelf number and token shown to student.

Admin approval required to finalize shelf assignment.

Students can request retrieval; admin confirms using shelf number and token.

Simple dashboards for users (students) and admins.

Status tracking with clear stages (requested, assigned, retrieval requested, collected).

Secure token-based verification for shelf ownership.

Admin messages for approvals and retrieval confirmations.

No timing/duration tracking (simplified for ease of use).

Users Included (Pre-configured for quick testing)
Username	Password	Role
lakshya	mypassword123	User
john	john123	User
admin	admin	Admin
(Please create these users manually via Django admin or create a script to initialize them.)

Installation & Setup
Clone the repository

bash
git clone <your-repo-url>
cd your_repo_folder
Create and activate a virtual environment

bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install django
Apply database migrations

bash
python manage.py makemigrations
python manage.py migrate
Create users (if not done)

bash
python manage.py createsuperuser
# Create 'admin' user with password 'admin'
# Create users 'lakshya' and 'john' with their passwords via admin panel or custom script
Run the development server

bash
python manage.py runserver
Access

User portal: /index/

Admin portal: /admin_shelves/

Usage
Students can assign shelves and see tokens.

Admin sees requests, approves by shelf number, confirms retrieval with shelf and token.

Students can only view their own shelf/token info and request statuses.

Admin messages shown only in admin dashboard.

Project Structure Overview
text
your_app/
├── models.py          # ShelfToken model without timing fields
├── views.py           # User/admin views with status handling and messages separated correctly
├── urls.py            # URL routes for user and admin endpoints
├── templates/
│   ├── index.html      # User dashboard template
│   └── admin_shelves.html # Admin dashboard template with approval forms and messages
├── templatetags/
│   └── __init__.py    # (empty, no custom filters anymore)
License
This project is developed by [Your Name] and is free to use under the MIT License.
