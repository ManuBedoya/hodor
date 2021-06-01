#!/usr/bin/python3
import requests


id = '2174'
iterators = 1024
data_user = {'id': id, 'holdthedoor': 'Submit'}
for i in range(1024):
    request = requests.post('http://158.69.76.135/level0.php', data=data_user)

print("Finish")
