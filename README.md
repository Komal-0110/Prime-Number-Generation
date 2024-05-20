# Prime-Number-Generation
This project provides a robust and efficient prime number generator accessible via a REST API built with Flask. It supports multiple generation strategies and logs each request to an in-memory database.

## Features

- Prime number generation within a specified range.
- Supports different generation strategies:
  - Basic Iterative Method
  - Sieve of Eratosthenes
  - Sieve of Sundaram
  - Segemented Sieve
- RESTful API for remote requests.
- Logs execution details, including timestamp, range, algorithm, time elapsed, and number of primes returned.
- Command-line interface for local generation.

## Requirements

- Python 3.8+
- Flask
- pymongo
- MongoDB

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Komal-0110/Prime-Number-Generation.git
    cd server
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the `.env` file:
    - Create a file named `.env` in the root directory of the project.
    - Add the following environment variables to the `.env` file:
      ```
      MONGODB_PWD=add mongodb password
      MONGODB_NAME=add mongodb username
      SECRET_KEY=add secret key
      ```

    Replace `MONGODB_PWD` with the actual MongoDB Password and `mongodb name` with the name of your MongoDB username.

## Usage

### Running the Server

Start the Flask server:
```bash
python app.py
```

The server will run on : 
```bash
http://127.0.0.1:5000/
```

For run command line interface : 
```bash
python PrimeNumberGeneration.py
```

For run Unit Test interface : 
```bash
python UnitTestCase.py
```