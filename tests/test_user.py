import unittest
from app .models import User

class UserModelsTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='password')
        
    def test_no_access_password(self):
        with self .assertRaises(AttributeError): 
           self.new_new_user.password
            
    def  test_password_verification(self):
         self.assertTrue(self.new_user.verify_password('password'))           