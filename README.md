# Secure Password CLI App
This is a command-line interface (CLI) Python app for securely storing and retrieving passwords using the cryptography Fernet library.

## Features
- Securely store passwords using Fernet encryption
- Generate random passwords with customizable length and character set
- View saved passwords
- Delete saved passwords
- Update saved passwords


## Installation
1. Clone the repository to your local machine:
```
git clone https://github.com/juankair/password-shield.git
```
2. Install the required dependencies using pip:
```
pip install -r requirements.txt
```

## Usage
To run the app, navigate to the project directory and run the main.py script:
```
python app.py
```
The app will display a menu with options for adding, viewing, updating, and deleting passwords.


Security
The app uses the Fernet library to encrypt passwords with a secret key. The key is stored securely in a local environment variable to prevent unauthorized access.

Contributions
Contributions to the app are welcome. To contribute, fork the repository and submit a pull request with your changes.

License
The app is released under the MIT License. See the LICENSE file for details.