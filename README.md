# Simple AES Algorithm

The project implements the S-AES(Simplified Advanced Encryption Standard) algorithm,
offering a comprehensive framework for encryption and decryption tasks across various
functionality levels.

**Demo Address**: http://8.137.22.197:5000/

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
    - [Run](#run)
    - [Test](#test)
- [Project Structure](#project-structure)
- [Contributors](#contributors)

## Introduction

The project begins with basic testing, implementing the S-AES algorithm to support encryption and decryption
of 16-bit data and keys through a user-friendly GUI. It expands functionality to support ASCII-encoded
strings, enhancing its practical usability. Additionally, the project explores multiple encryption
and decryption techniques, including double and triple encryption and decryption with various key lengths.
Finally, it employs the CBC mode for encrypting longer plaintexts, examining the effects of ciphertext
modification on decryption results.

## Dependencies

Before you set up, please ensure that you environment is set up with the necessary dependencies. The following
packages are essential for the project:

- python = 3.9.19
- Flask = 2.2.5
- Flask_Cors = 5.0.0
- numpy = 1.26.4

## Installation

To set up the project, you need to install the required dependencies. You can do this by running the following command:

```
pip install -r requirements.txt
```

## Usage

Once the installation is complete, you can start using the project. Here are the main commands to get you started.

### Run

To execute the project, use the following command:

```
flask run
```

Next, open your web browser and enter the following URL to
access the application:

```
http://127.0.0.1:5000/
```

### Test

To run the tests and ensure everything functions correctly, you can use the following command:

```
python -m unittest test.py
```

If you wish to run additional tests, please refer to the project's Application Program Interface
documentation(`API.pdf`).

## Project Structure

The structure of this project is designed to enhance maintainability and scalability. Below is a description of the main
files:

- `static/`: Contains all static files that are served directly to the client.
    - `css`: Stylesheets for the project, defining the visual appearance.
    - `images`: Contains images used in the application.
    - `js`: JavaScript files that provide interactivity and dynamic features.
    - `pdfs`: PDF documents related to the project.
- `templates`: Contains HTML templates for rendering the web pages.
- `app.py`: The main application file that initializes the Flask app, handles routing, and serves as the entry point for
  the application.
- `AES.py`: Contains the primary implementations of algorithms.
- `utils.py`: Provides utility functions commonly used in the project.
- `models.py`: Defines classes that encapsulate the result data structures.
- `constant.py`: Stores constant values used throughout the application.
- `result.py`: Handles the unified packaging of results returned by the application.
- `test.py`: Contains a set of tests cases for encrypting and decrypting strings.
- `API.pdf`: Provides detailed documentation of the API.
- `report.pdf`: Summarizes the test results of the S-AES algorithm.
- `requirements.txt`: Lists all the dependencies required for the project.
- `README.md`: Provides an overview of the project.

## Contributors

The project has two contributors:

- [Weizhe Chen](https://github.com/star-night-rain): Implemented the simple AES algorithm along with various
  adaptations, ensuring robust encryption and
  decryption functionality.
- [Jiafan Yu](https://github.com/NoTalentPlayer): Responsible for frontend development, enhancing the user interface and
  experience to ensure a seamless
  interaction with the application.
