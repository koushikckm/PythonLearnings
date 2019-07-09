import unittest
import test1
import test2
import test3
import test4

loader=unittest.TestLoader()
suite=unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test1))
suite.addTests(loader.loadTestsFromModule(test2))
suite.addTests(loader.loadTestsFromModule(test3))
suite.addTests(loader.loadTestsFromModule(test4))

runner=unittest.TextTestRunner(verbosity=3)
result=runner.run(suite)
   
if __name__=='__main__':
    unittest.main()