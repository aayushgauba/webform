
# Django Project with PostgreSQL Database

This repository contains a Django project integrated with a PostgreSQL database. The Django framework provides a robust foundation for web applications, while PostgreSQL ensures efficient and scalable data storage.

## Repository

The project repository can be found at: [https://github.com/aayushgauba/webform](https://github.com/aayushgauba/webform)

## Requirements

- Python (3.x recommended)
- Django (3.x or newer)
- PostgreSQL

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aayushgauba/webform.git
cd webform
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL Database

- Install PostgreSQL if not already installed.
- Create a new database for your Django project.

```sql
CREATE DATABASE your_database_name;
```

- Update the database settings in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Now, you can access the Django admin interface at `http://127.0.0.1:8000/admin/`.

## Project Structure

- `home/`: Main application directory.
- `home/models.py`: Defines database models.
- `home/views.py`: Contains view functions.
- `home/urls.py`: Defines URL patterns.
- `templates/`: Contains HTML templates.
- `static/`: Stores static files like CSS, JavaScript, and images.

## Credits

This project utilizes the [Bootstrap 5](https://getbootstrap.com/) framework for its frontend design and components. Bootstrap is a powerful and popular CSS framework that provides responsive and customizable components for web development.

```
