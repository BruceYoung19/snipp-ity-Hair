WebApp Testing Documentation
---
Overview
This document explains how to test the Snipp-ity Hair web application locally.
You’ll be running the development server to verify that the backend and frontend are working correctly.

Prerequisites

Before you begin, ensure that you have the following installed on your system:

Python 3.x

Django (installed via pip install django)

Any additional dependencies listed in requirements.txt

Steps to Test the Server
1. Open the Project Directory

Open a terminal or command prompt and navigate to the project directory:

```cd /snipp-ity-Hair```

2. Run the Development Server

Start the Django development server with the following command:

```python manage.py runserver```

3. Access the Web Application

Once the server starts, you’ll see output similar to:

Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.


Open a web browser and go to:

👉 http://127.0.0.1:8000/

You should now see the Snipp-ity Hair web app running locally.

4. Verify Functionality

Check that:

The homepage loads correctly

All navigation links work

Forms and buttons respond as expected

Any API calls or database interactions function without errors

If you encounter issues, check the terminal output for error messages.

5. Stop the Server

To stop the server, press:

CTRL + C

Troubleshooting
Issue	Possible Fix
python: command not found	Make sure Python is installed and added to your PATH
manage.py: no such file	Verify you are in the correct project directory
Server won’t start	Ensure all dependencies are installed via pip install -r requirements.txt
