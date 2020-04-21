# Mohamed Osman

## Technologies

### Python3/Flask

I used the technologies above as Flask is super lightweight. It allows for
quick creation of webservices and is super minimalistic.

### SQLAlchemy/SQLite

I used the technologies above as SQLite is an opensource SQL database that stores data to a text file on a device.
A huge advantage of that is that it offers great accessibility and provided
Python libraries are simple to use.

## IMPORTANT

Please delete `gifts.db` after every run of the application
or unit test to ensure validity and uniqueness of entries
since database is populated using json files on start up.

## Setup

1. Download this repo

2. Install the dependencies needed for the project defined in `setup.py`. From the root directory execute:

`pip3 install .`

3. Set the environment variable needed to start the Flask server:

`export FLASK_APP=gift_planner`

4. Run the application from the root directory:

`flask run`

5. You can now access the application at `localhost:5000`

## API

### Assign gift - `POST`

`/gifts/<name>`

Path variables - `name`

Body - N/A

Return codes - 200, 403, 404

## Return Codes

`200` - Gift assigned to employee successfully

`403` - Employee already received a gift

`404` - Employee does not exist/Gift already assigned

## Database Models

### Category - Represents categories/interests of each employee and its relating gift

Table with 4 columns: id, name, gift_name, employee_name

### Employee - Represents all employees

Table with 2 columns: id, name

### Gift - Represents gifts with assigned employee

Table with 3 columns: id, name, employee_name

## Considerations

- Flask is a single synchronous process, which means at most 1 request
being processed at a time. Therefore, we should not have an issue with multiple
employees assigning gifts to themselves. However, if it was synchronous,
an issue with the rush would be the same gift being assigned at the same time to multiple
employees.

- Try to have at least 1 gift for each interest of an Employee.

- Added a check to enforce that assigning a gift to an employee only occurs
if that gift has not been previously assigned to anyone else.

- We can add a boolean column in the Employee table "Returned" and re-assign the
gift for that specific employee. If that is successful, we can change "Returned"
column to "True", which means, an exchange has occurred for that specific employee.
Then, if that employee tries to return again, we check that "Returned" value,
if "True", we cannot complete the return.

## Unit Tests

From root directory, execute the following to run the tests:

`python3 -m pytest`