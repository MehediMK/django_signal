# Django Project with PostgreSQL and python-dotenv

This is a Django signal project with example.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- Git

## Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/MehediMK/django_signal.git
   cd django-with-postgresql
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**

   ```bash
   python manage.py runserver
   ```

   You should now be able to access the project at `http://127.0.0.1:8000/`.

## Additional Commands

- **Create a superuser**

  ```bash
  python manage.py createsuperuser
  ```

- **Run tests**

  ```bash
  python manage.py test
  ```

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have new features you want to add.