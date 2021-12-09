import os
import sys

# scriptpath = "../services/"
# sys.path.append(os.path.abspath(scriptpath))
# from operationsService import *
sys.path.insert(0,"..")
from services.operationsService import *

import unittest

class OperationTest(unittest.TestCase):
    def testSum(self):
        resp = elementarFunction (5, 5, '+')
        print (resp)
        self.assertEqual(resp[0], 10)

    def testSub(self):
        resp = elementarFunction (5, 5, '-')
        self.assertEqual(resp[0], 0)

    def testMult(self):
        resp = elementarFunction (5, 5, '*')
        self.assertEqual(resp[0], 25)

    def testDiv(self):
        resp = elementarFunction (5, 5, '/')
        self.assertEqual(resp[0], 1)

    def testLog(self):
        resp = transcendentFunction (14, 'LOG')
        self.assertEqual(resp[0], 2.6390573296152584)

    def testInverseX(self):
        resp = transcendentFunction (10, '1/X')
        self.assertEqual(resp[0], 0.1)

if __name__ == '__main__':
    unittest.main()
