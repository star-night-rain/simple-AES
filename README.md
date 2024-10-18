# Simple AES Algorithm

The project implements the S-AES(Simplified Advanced Encryption Standard) algorithm,
offering a comprehensive framework for encryption and decryption tasks across various
functionality levels.

## Table of Contents

- [Introduction](#introduction)
- [Dependencies](#dependencies)
- [Installment](#installment)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributor](#contributors)

## Introduction

The project begins with basic testing, implementing the S-AES algorithm to support encryption and decryption
of 16-bit data and keys through a user-friendly GUI. It expands functionality to support ASCII-encoded
strings, enhancing its practical usability. Additionally, the project explores multiple encryption
and decryption techniques, including double and triple encryption and decryption with various key lengths.
Finally, it employs the CBC mode for encrypting longer plaintexts, examining the effects of ciphertext
modification on decryption results.

## Dependencies

Before you get started, please ensure that you environment is set up with the necessary dependencies. The following
packages are crucial for the project to function correctly:

- python = 3.9.19
- Flask = 2.2.5
- Flask_Cors = 5.0.0
- numpy = 1.26.4

## Installment

To set up the project, you need to install the required dependencies. You can do this by running the following command:

```
pip install -r requirements.txt
```

## Usage

Once the installment is complete, you can start using the project. Here are the main commands to get you started.

### Run

To execute the project, use the following command:

```
flask run
```

### Test

To run the tests and ensure everything correctly, you can use the following command:

```
12
```

## Project Structure

The structure of this project is designed to enhance maintainability and scalability.Below is a description of the main
files:

- `app.py`: The main application file that initializes the Flask app, handles routing, and serves as the entry point for
  the application.
- `AES.py`: Contains the primary implementations of algorithms.
- `utils.py`: Provides utility functions commonly used in the project.
- `models.py`: Defines classes that encapsulate the result data structures.
- `constant.py`: Stores constant values used throughout the application.
- `result.py`: Handles the unified packaging of results returned by the application.
- `requirements.txt`: Lists all the dependencies required for the project.
- `README.md`: Provides an overview of the project.

## Contributors

The project has two contributors.

- `Weizhe Chen`: Implemented the simple AES algorithm along with various adaptations, ensuring robust encryption and
  decryption functionality.
- `Jiafan Yu`: Responsible for frontend development, enhancing the user interface and experience to ensure a seamless
  interaction with application.
