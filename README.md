# behaviour-driven-python-pytest-bdd
This repository contains example code written while following
*Behavior-Driven Python with pytest-bdd* course
from [Test Automation University](https://testautomationu.applitools.com/).

## Table of Contents
- [SetUp](#Setup)
- [IMPORTANT NOTE](#NOTE)
- [Purpose](#Purpose)
- [Reminder](#Reminder)


### Setup

1. Clone the repository.
   ```sh
    git clone https://github.com/victoriaajuwon/tau-api-testing-in-python.git
    ```
2. On another terminal, navigate to the root directory in your terminal
    ```sh
    cd tau-api-testing-in-python
    ```
3. You need to ensure you have virtual environment set up for the project
4. You can either use pipenv or pip, to use pipenv is installed. To install pipenv follow this [link](https://pipenv.pypa.io/en/latest/installation.html). To install pip, follow this [link](https://pip.pypa.io/en/stable/installation/)
5. Install dependencies using pipenv
    ```sh
    # Activate virtualenv
    pipenv shell
    # install
    pipenv install
    ```
6. Install dependencies using pip
    ```sh
    # Create virtualenv, inside the root directory, use the code below
    python -m venv venv
    # Activate virtualenv for windows
    .\venv\Scripts\activate
    # Activate virtualenv for Linux/MacOS
    source venv/bin/activate
    # Install dependecies one by one
    python -m pip install [dependency-name]
    # Install all dependecies using the requirements.txt
    python -m pip install -r requirements.txt
    ```
7. Run the test using pipenv
- Note: to run using the command for run all test, make sure your test file starts with a prefix 'test_'
    ```sh
    # Run the test
    pipenv run python -m pytest
    # Run a single test
    pipenv run python -m pytest [path/to/the/test/file]
    # Run by filtering with tags
    pipenv run python -k pytest "[tag-name]"
    ```
8. Run the test using pip
- Note: to run using the command for run all test, make sure your test file starts with a prefix 'test_'
    ```
    # Run the all test
    python -m pytest
    # Run a single test
    python -m pytest [path/to/the/test/file]
    ```


### NOTE

- #### Create Account with Test Automation University
  - To follow the tutorial, create an account on TestAutomation University [here](https://testautomationu.applitools.com/login.html)
  - Go to the Learning Path page [here](https://testautomationu.applitools.com/learningpaths.html?id=python-testing-path) and select Python path follow the courses in the order they are arranged. If you are familiar with python programming, you can skip the python tutorial and start with Behaviour Driven Python with pytest-bdd

### Purpose
The purpose of this project is to learn and understand how to use python to do Behaviour Driven Development especially  as a  tester.

### Reminder
The code for chapter 3 and chapter 4 is in note.txt