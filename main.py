import authentication
import landing
import json
import os
from cryptography.fernet import Fernet


landing.init()
# authentication.main()


# LIST FEATURE
# menu = [
#     {
#         'index': 1,
#         'name': 'Show Password'
#     }, {
#         'index': 2,
#         'name': 'Add Password'
#     }, {
#         'index': 3,
#         'name': 'Update Password'
#     }, {
#         'index': 4,
#         'name': 'Delete Password'
#     }
# ]

# print('Select Action:')
# for item in menu:
#     print('[' + str(item['index']) + '] ' + item['name'])











# arr = [
#     {
#         'platform' : 'google',
#         'username' : 'lambdasangkala45@gmail.com',
#         'password' : 'test12345'
#     }
# ]

# # key = Fernet.generate_key()
# key = os.environ.get('FERNET_KEY')

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