import os
import sys

# scriptpath = "../services/"
# sys.path.append(os.path.abspath(scriptpath))
# from operationsService import *
import importlib.util
 
def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
 
op = module_from_file("elementarFunction", "../services/operationsService.py")


import unittest

class OperationTest(unittest.TestCase):
    def testSum(self):
        resp = op.elementarFunction (5, 5, '+')
        print (resp)
        self.assertEqual(resp[0], 10)

    def testSub(self):
        resp = op.elementarFunction (5, 5, '-')
        self.assertEqual(resp[0], 0)

    def testMult(self):
        resp = op.elementarFunction (5, 5, '*')
        self.assertEqual(resp[0], 25)

    def testDiv(self):
        resp = op.elementarFunction (5, 5, '/')
        self.assertEqual(resp[0], 1)

    def testLog(self):
        resp = op.transcendentFunction (14, 'LOG')
        self.assertEqual(resp[0], 2.6390573296152584)

    def testInverseX(self):
        resp = op.transcendentFunction (10, '1/X')
        self.assertEqual(resp[0], 0.1)

if __name__ == '__main__':
    unittest.main()
