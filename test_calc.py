import unittest  # the unittest module is present in the standard library, no need to install it
import calc

class testCalc(unittest.TestCase):
    
    def test_add(self): # important ! the method has to start with "test_" or else it will to be tested ...
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-5,5),0) # good to add some edge cases: what about negative numbers ?
        self.assertEqual(calc.add(-10,-1),-11) # non integer ?

    def test_substract(self):
        self.assertEqual(calc.substract(10,5),5)
        self.assertEqual(calc.substract(-5,5),-10) 
        self.assertEqual(calc.substract(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-5,5),-25)
        self.assertEqual(calc.multiply(0,-3),0) 

    def test_divide(self): 
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-5,5),-1) 
        self.assertEqual(calc.divide(0,-3),0) 

    def test_divideError1(self): 
        self.assertRaises(ValueError,calc.divide,10,0) # we can also test if the divide method will raise a ValueError when we try to divide by 0.
        # Note that we are not passing the argument directly yo calc.divide ...
        # This is because if we give 10 and 0 as arguments to calc.divide, it will raise a ValueError before the test !

    def test_divideError2(self):
        # we can do the same thing but this time calling the calc.divide method in the regular way by using the "context manager"
        with self.assertRaises(ValueError): 
            calc.divide(10,0)
        
    


if __name__ == '__main__':
    unittest.main()