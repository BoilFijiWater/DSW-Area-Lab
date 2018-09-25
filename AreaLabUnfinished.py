import math #lets us use the math module 
import unittest #unittest module helps is test small sections of code 
 
def circleArea(radius): 
    return radius * radius *math.pi    

def rectArea(base, height):
    return 1

def trapArea(base1, base2, height):
    return 1

def triArea(base,height):
    return 1
    
	
class MyTest(unittest.TestCase): #using TestCase class from unittest module
    def testCircleArea(self):
        self.assertEqual(circleArea(5),25*math.pi)
        self.assertAlmostEqual(circleArea(10),100*math.pi)
    def testRectArea(self):
    self.assertEqual(rectangle(50),250*math)
    
    def testTrapArea(self):
    
    def testTriArea(self):
    
    
    
    