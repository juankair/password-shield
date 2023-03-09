import os
import sys
from hashlib import sha256


def main():
    secretKey = os.environ.get('SECRET_KEY')
    inputValidation = input('Proof you are Lambda: ')
    inputValidationEncode = sha256(inputValidation.encode('utf-8')).hexdigest()
    if secretKey != inputValidationEncode:
        print('GET THE F**K OUT OF HERE!!!')
        sys.exit()
    print('Heck Yeahh!')
