import unittest
from PyNumberApp import * 

# class TestFileType(unitTest.TestCase):
#     return
class TestAddNumbers(unittest.TestCase):
    def test_addNumber_positive(self):
        self.assertEqual(add_numbers([4,3,2]), 9)

class TestNumberType(unittest.TestCase):
    def test_Too_Big(self):
        self.assertLessEqual(add_numbers([3,4.5,4]), 99999999)
    def test_not_number(self):
        self.assertEqual(check_number([234,4433,2332]),)

#
# class TestHighLow(unitTest.TestCase):
#     def highest_num(self):
#         self.assertEqual(get_highest() )
#     def lowest_num(self):
#         self.assertEqual(get_lowest() )

if __name__ == '__main__':
    unittest.main()
