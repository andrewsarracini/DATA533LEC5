import maxval
import unittest


class TestMaxval(unittest.TestCase):
    def test_maxval(self):
        self.assertEqual(maxval.maxval(20, 10), 20)

    unittest.main(argv=[''], verbosity=2, exit=False)
