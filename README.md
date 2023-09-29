# Simple_OnlineStore

## Introduction

Welcome to the Simple_OnlineStore App! This is a simple online store application developed using Django, a high-level Python web framework. This README will guide you through the setup and usage of the app.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.6 or higher)
- Django (3.0 or higher)
- Git (optional, for cloning the repository)

## Installation

1. Clone the repository (or download and extract the ZIP file):

   ```
   git clone https://github.com/yourusername/django-online-store.git
   ```

2. Change into the project directory:

   ```
   cd django-online-store
   ```

3. Create a virtual environment (recommended):

   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Apply the database migrations:

   ```
   python manage.py migrate
   ```

7. Create a superuser (admin) account:

   ```
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```
   python manage.py runserver
   ```

## Usage

1. Open a web browser and navigate to `http://localhost:8000/admin/` to access the Django admin panel.

2. Log in using the superuser account created earlier.

3. You can manage items, categories, and orders through the admin panel.

4. To access the online store itself, go to `http://localhost:8000/store/`.

5. Users can browse products, add them to their cart, and place orders on the store's front-end.

## Features

- User authentication and authorization.
- Product and category management.
- Shopping cart functionality.
- Order processing and history.
- Responsive design for mobile and desktop.

## Contributing

If you would like to contribute to this project, because I would like help to intergrrate payments please follow the [contributing guidelines](CONTRIBUTING.md).

## Acknowledgments

- Thanks to the Django community for creating an amazing web framework.
- Special thanks to our contributors for their efforts in developing and maintaining this project.
- And above all special thanks to 'Youtube University'😂
  
Happy shopping 🛒🌟
