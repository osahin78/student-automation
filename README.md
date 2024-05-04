# student-automation

As part of the school council, we are seeking to develop a REST API to manage and store student data in a database. This includes names, student numbers, and their corresponding grades by course code. When multiple entries exist for a single course, the API should calculate and store the average grade for that course.

# installation

```bash
git clone https://github.com/osahin78/student-automation.git
cd student-automation
python -m venv venv
venv\Scripts\activate.bat
python -m pip install Django
python -m pip install --upgrade pip
code .

## open a terminal on visual studio code

cd school_council
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
