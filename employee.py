import requests 

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def applyraise(self):
        self.pay = self.pay * self.raise_amt


    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad response'


def __main__():

    emp1 = Employee('Jracob','Garluc',12)
    emp2 = Employee('Birtul','Choufrai',1000)

__main__()