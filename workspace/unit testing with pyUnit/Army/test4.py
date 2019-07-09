import unittest
from soldier import Soldier

class TestEligibility(unittest.TestCase):
    candidate4=Soldier(18)
    
    def test_four(self):
        self.assertEqual(self.candidate4.checkagelimit(),True)
        
if __name__=='__main__':
    unittest.main()