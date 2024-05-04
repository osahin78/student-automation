# student-automation

As part of the school council, we are seeking to develop a REST API to manage and store student data in a database. This includes names, student numbers, and their corresponding grades by course code. When multiple entries exist for a single course, the API should calculate and store the average grade for that course.

# Installation on Windows

open command prompt </br>
cd C:\Installation Folder

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

## TEST

```bash
curl --location '127.0.0.1:8000/api/' \
--header 'Content-Type: application/json' \
--data '{
    "name": "",
    "surname": "Yilmaz",
    "stdNumber": "B012X00055",
    "grades": [
        {
            "code": "MT101",
            "value": 90
        },
        {
            "code": "PH101",
            "value": 75
        },
        {
            "code": "CH101",
            "value": 60
        },
        {
            "code": "MT101",
            "value": 70
        },
        {
            "code": "HS101",
            "value": 65
        }
    ]
}'
```
