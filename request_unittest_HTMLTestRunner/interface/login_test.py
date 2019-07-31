import unittest
import  requests
r =requests.post('http://127.0.0.1:8000/login_action/',data={'username':'admin','password':'admin123456'})
print(r.text)