import requests
import json
import re
import base64
register_image_file = '1'
register_ufile_id = ''
verify_image_file = ''
verify_ufile_id = ''
with open('2.jpg', 'rb') as file:
    register_image_file = str(base64.b64encode(file.read()))[2:-1]
with open('2.jpg', 'rb') as file:
    verify_image_file = str(base64.b64encode(file.read()))[2:-1]

# print(''.join(["1",register_image_file, register_ufile_id, verify_image_file, verify_ufile_id, "J87m!AF@56CLLD#C612d31a7030g1+5"]))
sign = ''.join(["1",register_image_file, register_ufile_id, verify_image_file, verify_ufile_id, "RealMe", "J87m!AF@56CLLD#C612d31a7030g1+5"])
import hashlib

m = hashlib.md5()
m.update(sign.encode('utf-8'))
sign=m.hexdigest()
dict_data = {"customer_id": "1", "sys_id": "RealMe", "sign": sign,
             "register_image_file": register_image_file, "register_ufile_id":register_ufile_id,
              "verify_image_file": verify_image_file, "verify_ufile_id": verify_ufile_id,
             }
import time
s = time.time()
# print(dict_data)
# r = requests.post('http://127.0.0.1:8625/jarvis-face', json=dict_data)
r = requests.post('http://192.168.3.3:8628/jarvis-face', json=dict_data)
print(r.text)
e = time.time()
print(e - s)


