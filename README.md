# KAMI-Assessment-Ravi
This is the repository of KAMI Assessment Test for Ravi

# How to use the application
## Instalation
1. Install all dependencies to run the application.
`pip install -r requirements.txt`
2. Migrate the application migrations script.
`python manage.py migrate`
3. Collect the application static files to run the application swagger.
`python manage.py collectstatic`

## Run the application
1. To run the application, simply just run the command bellow:
`python -m gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker`
And the application will be run at http://127.0.0.1:8000
2. To run the application test, please run the command below:
`coverage run --source='.' manage.py test`
or if you want to run specific application test, you can run the command below:
`coverage run --source='.' manage.py test [application name]`
The application name options are `aircraft_api` and `user_api`.
3. To run the code coverage, just run the command below:
`coverage report`

## API Documentation
API Documentation can be found at [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
