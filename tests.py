from solver import *
import unittest

class TestMethods(unittest.TestCase):

    def test_legal_moves(self):
        a = ImageScrambleGame(gsize=3, seednum=2)
        self.assertTrue([0, 3] == legal_moves(a))

        b = ImageScrambleGame(gsize=4, seednum=3)
        self.assertTrue([1, 0 , 3, 2] == legal_moves(b))

        c = ImageScrambleGame(gsize=5, seednum=4)
        self.assertTrue([3, 2] == legal_moves(c))
        return

    def test_h_hist(self):
        a = ImageScrambleGame(gsize=3, seednum=2)
        self.assertTrue(16 == h_dist(a))

        b = ImageScrambleGame(gsize=4, seednum=3)
        self.assertTrue(39 == h_dist(b))

        c = ImageScrambleGame(gsize=5, seednum=4)
        self.assertTrue(70 == h_dist(c))
        return

if __name__ == '__main__':
    unittest.main()