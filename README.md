# Fyle Backend Challenge

## Challenge outline

This challenge involves writing a backend service for a classroom. The challenge is described in detail [here](./Application.md)


## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```
### Reset DB

```
export FLASK_APP=core/server.py
rm core/store.sqlite3
flask db upgrade -d core/migrations/
```
### Docker
Execute the following command to start the server in a docker container
```
docker compose up --build
```
Similarily to stop the container, execute
```
docker compose down
```
 
### Start the 

### Run Tests

```
pytest -vvv -s tests/

# for test coverage report
# pytest --cov
# open htmlcov/index.html
```
### Screenshot
![Screenshot](screenshot/ss.png)

