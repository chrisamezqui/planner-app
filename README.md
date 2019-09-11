# Planning Web Application
Cooler name coming soon...

## Dependencies
1. Python 3.7+ (with pip and venv which should come with python installation)
1. Docker tool-kit
1. Yarn (dependency manager)

## Start Up Instructions
1. Enter `webServices/` directory to set up back-end server and database
1. Run `python -m venv ./appenv`
1. `source appenv/Scripts/activate`
1. `pip install -r appenv/requirements.txt`
1. To launch docker container running MongoDB, run `docker-compose up`
1. To launch flask server, run `python -m app`
1. Go to `app/http/web/app/` directory to set up front-end react.js
1. Run `yarn install`
