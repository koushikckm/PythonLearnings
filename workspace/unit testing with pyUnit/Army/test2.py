import unittest
from soldier import Soldier

class TestEligibility(unittest.TestCase):
    candidate1=Soldier(23)
    
    def test_one(self):
        self.assertEqual(self.candidate1.checkagelimit(),True)
        
if __name__=='__main__':
    unittest.main()