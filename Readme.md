Assignment
====================

## Author

__Ahsanuzzaman Khan__

## Project Description
You need to create a simple application which:

1. Upload a csv.
2. Parse that csv and store data to database.
3. Write test cases.
4. Application should be dockerised.


## Requirements
- Python 3.8
- PostgreSQL
- Django
- Django REST Framework
- Faker
- Docker
- Celery
- Redis

## Developer requirements
- Factory Boy
- Pytest Django

## Installation
- Install `docker`
- Download this git repo
- Then go to project directory
- And run `make setup`

## To Run project
Go to project folder and run 
- `make runserver`

## Test project
Go to project folder and run 
- `make test`

## Project urls
- For apis: `http://localhost:8100/`

## Project coverage
- Write testcase with above 80% of coverage
- CSV uploaded successfully
- Though it's a large file, so I call a background task using celery
- Project is dockerise and instruction has given at Readme file.
