import unittest
from employee import Employee

class testEmployee(unittest.TestCase):

    # this example works, but can be improved ...
    # if the Employee class is modified, we have to rewrite every single test ...
    # a way around is shown in test_employee2

    def test_email(self):
        emp1 = Employee('Toto','Luc',1000)
        emp2 = Employee('Lala','Tuc',1000)

        self.assertEqual(emp1.email,'Toto.Luc@email.com')
        self.assertEqual(emp2.email,'Lala.Tuc@email.com')

        emp1.first  = 'John'
        emp2.first = 'Jane'

        self.assertEqual(emp1.email,'John.Luc@email.com')
        self.assertEqual(emp2.email,'Jane.Tuc@email.com')

    def test_fullname(self):
        emp1 = Employee('Toto','Luc',1000)
        emp2 = Employee('Lala','Tuc',1000)

        self.assertEqual(emp1.fullname,'Toto Luc')
        self.assertEqual(emp2.fullname,'Lala Tuc')

        emp1.first  = 'John'
        emp2.first = 'Jane'

        self.assertEqual(emp1.fullname,'John Luc')
        self.assertEqual(emp2.fullname,'Jane Tuc')

    def test_applyraise(self):
        emp1 = Employee('Toto','Luc',1000)
        emp2 = Employee('Lala','Tuc',1000)

        emp1.applyraise()
        emp2.applyraise()

        self.assertEqual(emp1.pay,1050)
        self.assertEqual(emp2.pay,1050)



if __name__ == '__main__':
    unittest.main()