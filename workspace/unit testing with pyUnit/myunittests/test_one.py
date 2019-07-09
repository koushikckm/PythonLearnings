import unittest
from one import *

class myTestClassName(unittest.TestCase):
    def test_unittest1(self):
        self.assertEqual(checkfunction1(16,12),True)
        
    def test_unittest2(self):
        self.assertEqual(checkfunction2("Everyday"),True)
        
    #def test_unittest3(self):
        #self.assertEqual(checkfunction2("Monday"),True)
        
if __name__=='__main__':
    unittest.main()