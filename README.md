# Flask Quickstart for AppEngine
This repo provides a quickstart for running flask on a local environment, or in production using Google's AppEngine
## Requirements
* Python 2.7 (May work with Python 3, but has not been tested as of yet)
* Flask
* If wanting to test on the AppEngine local environment, please follow the steps outlined [here](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env)
##Configuring the Application
* `vi app/main.py`
* Update the port number at the `run` command to the desired port for the local server
## Starting the Application Locally
* `cd app`
* `python main.py`
* The application should now be available at a given port
---
# Spark
Spark is a command line helper tool while developing an application in flask
## Usage
`python spark.py <group>:<command> <*argument*>`
## Currently Available Commands
### Tests
`test:create`: Creates a new test file
`test:single <name>`: Runs a single test file by name
`test:all`: Runs all test files in the `tests` directory
### Controllers
`controller:create`: Creates a new controller and register's its blueprint and url prefix
## Commands on the Roadmap
### Models
Ability to create models
### Migrations
Ability to create, execute, and rollback database migrations
### Seeds
Ability to create and execute database seeders

