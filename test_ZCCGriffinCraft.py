import unittest
import ZCCGriffinCraft

class TestZCC(unittest.TestCase):

    def test_tix_info(self):
        self.assertRaises(ValueError, tix_info, None)
    def test_print_tix(self):
        tempArr = []
        #Error for invalid min
        self.assertRaises(ValueError, print_tix, -1, 10, tempArr)
        #Error for invalid max
        self.assertRaises(ValueError, print_tix, 0, 1000000000, tempArr)
        #Error for null ticket arr
        self.assertRaises(ValueError, print_tix, 0, 100, None)
        #Error for ticket arr with no values
        self.assertRaises(ValueError, print_tix, 0, 0, tempArr)
        