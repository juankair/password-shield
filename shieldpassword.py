import json
import os
from cryptography.fernet import Fernet
from prettytable import PrettyTable
from datetime import datetime

# arr = [
#     {
#         'platform': 'google',
#         'username': 'lambdasangkala45@gmail.com',
#         'password': 'test12345'
#     }
# ]

# # key = Fernet.generate_key()

# fernet = Fernet(key)
# data_enc = json.dumps(arr)
# ex = data_enc.encode()
# encrypted = fernet.encrypt(ex)

# # MODIFY FILE
# f = open("secure.lambda", "w")
# f.write(encrypted.decode())
# print(encrypted)

# # READ FILE
# f = open("secure.lambda", "r")
# todec = f.read().encode()
# print(todec)

# decrypted = fernet.decrypt(todec)
# print(decrypted.decode())


def showPassword():
    key = os.environ.get('FERNET_KEY')
    fernet = Fernet(key.encode())

    # Fetch Encrypt Data
    f = open("secure.lambda", "r")
    todec = f.read().encode()
    decrypted = fernet.decrypt(todec).decode()
    dataPassword = json.loads(decrypted)
    # print(decrypted)
    t = PrettyTable(['Platform', 'Group Type', 'Host', 'Username',
                    'Password', 'Last Update'])
    for item in dataPassword:
        t.add_row([item['platform'], item['group'], item['host'], item['username'],
                  item['password'], item['createdAt']])
    print(t)


def addPassword():
    key = os.environ.get('FERNET_KEY')
    fernet = Fernet(key.encode())

    platform = input("Input Platform Name : ")
    group = input("Input Group (Organization/Personal) : ")
    host = input('Input Host : ')
    username = input("Input Username : ")
    password = input("Input Password : ")

    now = datetime.now()
    createdAt = now.strftime("%d/%m/%Y %H:%M:%S")

    data = [
        {
            'platform': platform,
            'group': group,
            'host': host,
            'username': username,
            'password': password,
            'createdAt': createdAt,
            'trackingChanges': []
        }
    ]

    data_enc = json.dumps(data)
    ex = data_enc.encode()
    encrypted = fernet.encrypt(ex)
    # # MODIFY FILE
    f = open("secure.lambda", "w")
    f.write(encrypted.decode())
    print(encrypted)


def deletePassword():
    key = os.environ.get('FERNET_KEY')
    fernet = Fernet(key.encode())

    # # Fetch Encrypt Data
    # f = open("secure.lambda", "r")
    # todec = f.read().encode()
    # decrypted = fernet.decrypt(todec).decode()
    # dataPassword = json.loads(decrypted)
    # # print(decrypted)
    # t = PrettyTable(['Index','Platform', 'Username', 'Password'])
    # idx = 0
    # for item in dataPassword:
    #     idx = idx + 1
    #     t.add_row([idx,item['platform'],item['username'],item['password']])
    # print(t)
    # platform = input("Select Index to Remove : ")

    # # MODIFY FILE
    ex = []
    encrypted = fernet.encrypt(json.dumps(ex).encode())
    f = open("secure.lambda", "w")
    f.write(encrypted.decode())
    print(encrypted)
