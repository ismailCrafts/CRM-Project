# 📌 CRM Project

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)  
![Django](https://img.shields.io/badge/Django-5.2.4-green?logo=django)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)  

*Description*

A **Django-based Customer Relationship Management (CRM) Project** is a Django-based Customer Relationship Management application that lets users manage customer data efficiently.

It supports **adding**, **updating**, **deleting**, and **searching** customer records, along with **profile images** and *detailed info*.

The app includes *authentication* (**login**, **logout**, **registration**) and an admin panel for easy management.

---

## 🚀 Features

- ✅ User Authentication – Login, Logout, Registration  
- ✅ Customer Management – Add, Update, Delete, Search customers 
- ✅ Profile Images – Store and display customer profile photos
- ✅ Media Uploads – Images stored in /Uploads/pictures/  
- ✅ Search Functionality – By first name, last name, or email  
- ✅ Admin Panel – Manage records through Django admin  
- ✅ Database- PostgreSQL Database Support
- ✅ Dynamic URLs – View customer details by ID
- ✅ Local Development – Runs on http://127.0.0.1:8000

---

## 📂 Project Structure

```

CRM_Project/
│
├── crmapp/
│   ├── migrations/
│   ├── static/
│   │   └── default/            # Default profile images
│   ├── templates/              # HTML templates
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── crmproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Uploads/                    # Uploaded media files
│   └── pictures/               # Profile pictures
│
├── db.sqlite3                   # (If using SQLite)
├── manage.py
└── requirements.txt


```


---
## Installation

**1. Clone the repository**
```
git clone https://github.com//ismailCrafts//CRM_Project.git
cd CRM_Project
```

**2. Create and activate virtual environment**
```
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux

```

**3. Install dependencies**
```
pip install -r requirements.txt

```

**4. PostgreSQL Setup**

Make sure PostgreSQL is installed and running.
Create a database and update ```crmproject/settings.py```:


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'crm_database',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

**5. Run migrations**
```
python manage.py makemigrations
python manage.py migrate

```

**6. Create a superuser**
```
python manage.py createsuperuser

```

**7. Run the development server**
```
python manage.py runserver

```
*Visit: http://127.0.0.1:8000*

---

## Media & Static Files

* Static Files: Located in ```crmapp/static/```

* Media Files: Uploaded images stored in ```Uploads/pictures/```

* Config in ```settings.py```:

```
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/Uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'Uploads')
```

---

## Usage

1. Register or log in.

2. Add new customers with details and profile images.

3. View all customers in a table.

4. Click the ID link to see detailed customer info.

5. Edit or delete records as needed.

6. Search customers using the search bar.


















