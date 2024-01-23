# Dinero_EMP_Task
An Employee Management System in Django-Python

This Django-based Employee Management System has mainly three core modules:

1. **Employee Management:** Facilitates the addition, modification, and removal of employees. Each employee possesses essential attributes such as Name, Email, Address, Designation, Reporting Manager, and Department.

2. **Department Management:** Manages departments, allowing administrators to add, update, and delete records. Department attributes include Name and Floor.

3. **Employee Salary Management:** Administers employee salaries over time, supporting the addition, modification, and deletion of salary entries within specified date ranges.

## Features

### Employee Management Module

- **Admin Page:** Enables administrators to seamlessly manage employee records.
- **Reporting Hierarchy Page:** Illustrates the reporting hierarchy within each department, delineating the organizational structure.

### Department Management Module

- **Admin Page:** Empowers administrators to handle department records efficiently.
- **Reporting Hierarchy Page:** Visualizes the reporting hierarchy within each department, showcasing managers, TLs, and associates.

### Employee Salary Management Module

- **Admin Page:** Streamlines the process of adding, updating, and deleting salary entries.
- **Department-wise Salary Report Page:** Provides insights into department-wise salary costs within specified date ranges.

## Tech Stack

- **Python:** Primary programming language.
- **Django:** Web framework for building the application.
- **Database:**  MySQL.
- **Frontend:** BootStrap and JavaScript.

## Setup Instructions

1. Clone the repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Configure the database settings in the `settings.py` file.
4. Run migrations using `python manage.py migrate`.
5. Create a superuser for the Django admin using `python manage.py createsuperuser`.
6. Run the development server with `python manage.py runserver`.
7. Access the Django admin at `http://localhost:8000/admin/` and login with the superuser credentials.

## Project Structure

- **Tarique_Khan_Emp/:** Main Django project folder.
  - **employee/:** Django app for the Employee Management System.
    - **models.py:** Houses database models for employees, departments, and salary entries.
    - **views.py:** Manages the logic for rendering views.
    - **admin.py:** Customizes the Django admin interface.
    - **templates/:** Stores HTML templates for rendering views.
    - **static/:** Repository for static files such as CSS and JavaScript.

## Estimated Time

This project is expected to take approximately one week to complete. The breakdown of tasks and the approach are detailed in the project management plan.

## Contact

For any clarifications or assistance, please feel free to contact Tarique Khan at tarrrique@gmail.com.
