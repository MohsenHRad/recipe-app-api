"""
 Sample Test
"""

from django.test import SimpleTestCase

import calc
import list_sorter


class CalcTests(SimpleTestCase):
    """ Test the Calc module"""

    def test_add_numbers(self):
        """ Test adding numbers to geather. """
        res = calc.add(5, 6)

        return self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """ Test Subtracting Numbers"""
        res = calc.subtract(10, 15)

        return self.assertEqual(res, 5)


class SortListTests(SimpleTestCase):
    list_1 = [4, 3, 1, 7, 6, 2, 9, 3, 2, 1, 2]
    """ Test the SortList module"""

    def test_remove_duplicate(self):
        res = list_sorter.remove_duplicates(self.list_1)
        # print(res)
        return self.assertEqual(res, [1, 2, 3, 4, 6, 7, 9])
