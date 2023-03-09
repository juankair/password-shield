import json
import os
from cryptography.fernet import Fernet


def showPassword():
    arr = [
        {
            'platform': 'google',
            'username': 'lambdasangkala45@gmail.com',
            'password': 'test12345'
        }
    ]

    # key = Fernet.generate_key()
    key = os.environ.get('FERNET_KEY')

    fernet = Fernet(key)
    data_enc = json.dumps(arr)
    ex = data_enc.encode()
    encrypted = fernet.encrypt(ex)

    # MODIFY FILE
    f = open("secure.lambda", "w")
    f.write(encrypted.decode())
    print(encrypted)

    # READ FILE
    f = open("secure.lambda", "r")
    todec = f.read().encode()
    print(todec)

    decrypted = fernet.decrypt(todec)
    print(decrypted.decode())
