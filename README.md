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
or to run specific application test, run the command below:
`coverage run --source='.' manage.py test [application name]`
The application name options are `aircraft_api` and `user_api`.
3. To run the code coverage, just run the command below:
`coverage report`

## Using the application
1. Create a new user with POST method the following URL:
`http://127.0.0.1:8000/v1/user/registration/`
Set the request parameters with JSON format as follows:
```
{
    "username": [username: string of username],
    "email": [email: string of email address],
    "password": [password: string of password]
}
```
If the user registration is successful, it will return the response as follows:
```
{
    "message": "User [username: string of username] created successfully",
    "status": "200"
}
```
2. Login the user to get the application token and refresh token with POST method the following URL:
`http://127.0.0.1:8000/v1/user/login/`
Set the request parameters with JSON format as follows:
```
{
    "username": [username: string of username],
    "password": [password: string of password]
}
```
If the user login is successful, it will return the response as follows:
```
{
    "refresh": [refresh: string of refresh token],
    "access": [access: string of access token],
}
```
3. Send the aircraft list request with POST method the following URL:
`http://127.0.0.1:8000/v1/aircraft/calculation/list/`
Set the authorization header as follows:
`Authorization: Bearer [string of access token]`
Set the request parameters with JSON format as follows:
```
{
    "aircraft": [
        ...,
        {
            "aircraft_id": [aircraft_id: integer of aircraft_id],
            "aircraft_passenger": [aircraft_passenger: number of aircraft_passenger]
        },
        ...
    ]
}
```
If the request is successful, it will return the response as follows:
```
{
    "aircraft": [
        ...,
        {
            "aircraft_id": [aircraft_id: integer of aircraft_id],
            "aircraft_passenger": [aircraft_passenger: number of aircraft_passenger],
            "aircraft_total_fuel_consumption_per_minute": [aircraft_total_fuel_consumption_per_minute: number of fuel consumption per minute],
            "aircraft_maximum_flight_time_in_minutes": [aircraft_maximum_flight_time_in_minutes: number of aircraft maximum flight time in minutes]
        },
        ...
    ]
}
```
4. To refresh the access token, send the refresh token request with POST method the following URL:
`http://127.0.0.1:8000/v1/user/login/refresh/`
Set the request parameters with JSON format as follows:
`{"refresh": [refresh: string of refresh token]}`
If the refresh token request is successful, it will return the response as follows:
`{"access": [access: string of access token]}`
5. Optionally, the application also could handle single aircraft request with POST method the following URL:
`http://127.0.0.1:8000/v1/aircraft/calculation/list/`
Set the authorization header as follows:
`Authorization: Bearer [string of access token]`
Set the request parameters with JSON format as follows:
```
{
    "aircraft_id": [aircraft_id: integer of aircraft_id],
    "aircraft_passenger": [aircraft_passenger: number of aircraft_passenger]
}
```
If the request is successful, it will return the response as follows:
```
{
    "aircraft_id": [aircraft_id: integer of aircraft_id],
    "aircraft_passenger": [aircraft_passenger: number of aircraft_passenger],
    "aircraft_total_fuel_consumption_per_minute": [aircraft_total_fuel_consumption_per_minute: number of fuel consumption per minute],
    "aircraft_maximum_flight_time_in_minutes": [aircraft_maximum_flight_time_in_minutes: number of aircraft maximum flight time in minutes]
}
```

## API Documentation
Full API Documentation can be found at [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
