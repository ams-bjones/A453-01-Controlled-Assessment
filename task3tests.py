import task3 as t3
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        a = '0000000001'
        b = 7#put expected check digit here
        #getCD returns the original ISBN Number (a) as well as the check digit (b)
        assert(t3.getCD(a)== a+b )#test 1 fails answer is not as expected

if __name__ == '__main__':
    unittest.main()
