import unittest
from my_cli import MyCli
import matplotlib.image as mpimg
from io import StringIO
import sys


class MyCliTestCase(unittest.TestCase):
    def test_do_pyr_class_diagram(self):
        my_cli = MyCli()
        my_cli.do_pyr_class_diagram('test test.py')
        actual_output = mpimg.imread('classes_test.png')      
        expected_output = mpimg.imread('classes_test_for_test_case.png')
        comparison = actual_output == expected_output
        equal_arrays = comparison.all()
        self.assertEqual(equal_arrays, True)

    def test_do_validate_class_contents(self):
        my_cli = MyCli()
        my_cli.do_validate_class_contents('test.py')
        actual_output = mpimg.imread('validate_test.png')      
        expected_output = mpimg.imread('validate_test_for_test_case.png')
        comparison = actual_output == expected_output
        equal_arrays = comparison.all()
        self.assertEqual(equal_arrays, True)        

if __name__ == '__main__':
    unittest.main()
