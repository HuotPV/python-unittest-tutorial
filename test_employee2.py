import unittest
from unittest.mock import patch
from employee import Employee

class testEmployee(unittest.TestCase):

    # An improved version of test_employee1, using setUp and tearDown.
    # setUp is called before each test, tearDown is called after each test.

    def setUp(self):
        print('setUp') # just to show that setUp is called beforeeach test
        self.emp1 = Employee('Toto','Luc',1000) # to have access to emp1 and emp2 instances within the tests, we put them as attributes of self.
        self.emp2 = Employee('Lala','Tuc',1000)

    def tearDown(self):
        print('tearDown\n') # just to show that teardown is called beforeeach test
             # here we do not need the tearDown and only keep it as an illustration.
             # it can for instance be to remove files created during the tests.

    # we can also to a batch of code before doing any test and after all the tests are done
    # this is done by defininf a setUp and tearDown class method

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')


    def test_email(self):
        print('test email')
        self.assertEqual(self.emp1.email,'Toto.Luc@email.com') # since emp1 and emp2 are now attributes, we have to call them as self.emp1 ...
        self.assertEqual(self.emp2.email,'Lala.Tuc@email.com')

        self.emp1.first  = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.email,'John.Luc@email.com')
        self.assertEqual(self.emp2.email,'Jane.Tuc@email.com')

    def test_fullname(self):
        print('test fullname')

        self.assertEqual(self.emp1.fullname,'Toto Luc')
        self.assertEqual(self.emp2.fullname,'Lala Tuc')

        self.emp1.first  = 'John'
        self.emp2.first = 'Jane'

        self.assertEqual(self.emp1.fullname,'John Luc')
        self.assertEqual(self.emp2.fullname,'Jane Tuc')

    def test_applyraise(self):
        print('test applyraise')

        self.emp1.applyraise()
        self.emp2.applyraise()

        self.assertEqual(self.emp1.pay,1050)
        self.assertEqual(self.emp2.pay,1050)

    def test_monthly_schedule(self): # the method monthly schedule depends upon the availability of a website, but we do not want the tests to fail
                                     # if the code is correct but the website is down, so we will "mock" the method with predefined values and see if 
                                     # the code is indeed behaving as intented.
        with patch('employee.requests.get') as mocked_get: 
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Sample text'

            schedule = self.emp1.monthly_schedule('May')

            mocked_get.assert_called_with('http://company.com/Luc/May') # check that the mocked_get has indeed been called by the right URL.

            self.assertEqual(schedule,'Sample text')

            mocked_get.return_value.ok = False

            schedule = self.emp2.monthly_schedule('June')

            mocked_get.assert_called_with('http://company.com/Tuc/June') # check that the mocked_get has indeed been called by the right URL.

            self.assertEqual(schedule,'Bad response')

if __name__ == '__main__':
    unittest.main()