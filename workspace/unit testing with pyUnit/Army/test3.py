import unittest
from soldier import Soldier

class TestEligibility(unittest.TestCase):
    candidate3=Soldier(24)
    
    def test_three(self):
        self.assertEqual(self.candidate1.checkagelimit(),True)
        
if __name__=='__main__':
    unittest.main()