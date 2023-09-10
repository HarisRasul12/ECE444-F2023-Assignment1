#forgot to commit seperately first time, 2nd time around did
#Following unit test format form the following website - in the past I did my own unittest, but now following this methodology:
############Unit test format Source: https://geekflare.com/unit-testing-with-python-unittest/########
from utils import *
import unittest


class util_tests(unittest.TestCase):
    def test_reveresed(self):
        self.assertEqual(utils.reversed(25),52)
        self.assertEqual(utils.reversed(-25),-52)
        self.assertEqual(utils.reversed("25"),52)
        self.assertEqual(utils.reversed(25.0),0.52)
        self.assertFalse(utils.reversed("hello"))


    def test_formatter(self):
        self.assertEqual(utils.formatter(25),('0b11001','0o31'))
        self.assertEqual(utils.formatter(-25),('-0b11001','-0o31'))
        self.assertEqual(utils.formatter("25"),('0b11001','0o31'))
        self.assertEqual(utils.formatter(25.0),('0b11001','0o31'))
        self.assertFalse(utils.formatter("hello"))
        self.assertEqual(utils.formatter(25.0),('0b11001','0o31'))

if __name__ == "__main__":
    unittest.main()
