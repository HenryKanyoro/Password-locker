import unittest
from user import User
from user import Creditials

class TestClass(unittest.TestCase):
  
    def setUp(self):
        """
        a method that runs before the test
        """
        self.new_user = User('kerry1','joker1234')

    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
      
        self.assertEqual(self.new_user.username,'kerry1')
        self.assertEqual(self.new_user.password,'joker1234')

    def test_save_user(self):
        '''
        test case to check if the new instance of the user object has been created
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCreditials(unittest.TestCase):   
    """
    A test class that defines test cases for credentials class

    """ 
    def setUp(self):
        '''
        Method that runs before each individual credentials test methods run.
        '''
        self.new_creditials = Creditials('kerry','kerry1','joker1234')

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Creditials.creditials_list = []

    def test_details(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        
        self.assertEqual(self.new_creditials.account,'kerry')
        self.assertEqual(self.new_creditials.username,'kerry1')
        self.assertEqual(self.new_creditials.password,'joker1234') 

    def test_save_credentials(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_creditials.save_user_creditials()
        self.assertEqual(len(Creditials.creditials_list),1)

    def test_save_many_account(self):
