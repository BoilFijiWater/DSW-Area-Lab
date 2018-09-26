import math #lets us use the math module 
import unittest #unittest module helps is test small sections of code 
 
def circleArea(radius): 
    """returns the area of a circle with the given radius"""
    return radius * radius *math.pi 

def rectArea(base, height):
    if base<0 or height<0:
        return -1
    return base*height
    """returns the base and height"""
   
def trapArea(base1, base2, height):
    return height *(base1 + base2) / 2
    """returns the height, base1, base2"""
    return 1
     
    
def triArea(base,height):
    return base * height / 2
    """returns returns the base and height"""
    return 1
    
	
class MyTest(unittest.TestCase): #using TestCase class from unittest module
    def testCircleArea(self):
        self.assertEqual(circleArea(5),25*math.pi)
        self.assertAlmostEqual(circleArea(10),100*math.pi)
    
    def testRectArea(self):
        self.assertEqual(rectArea(-3,-2),-1)
        self.assertEqual(rectArea(6,2),18)
    
    def testTrapArea(self):
        self.assertEqual(trapArea(50,2,1),(50*2)/1)
        self.assertEqual(trapArea(6,4, 3),(6*4)/3)
    
    def testTriArea(self):
        self.assertEqual(triArea(3,20),(3*20)/2)
        self.assertEqual(triArea(19,6),(19*6)/2)
        
        #Formula for area of a circle: radius * radius * PI
        #Formula for area of a rectangle: base * height
        #Formula for area of a trapezoid: height * (base1 + base2) / 2
        #Formula for area of a triangle: base * height / 2