import unittest
import context

from simulator import core as unit


class TestCore(unittest.TestCase):

    def test_config_parsing(self):
        expected_value = 1

        actual_value = unit.foobar()

        self.assertEqual(expected_value, actual_value)


if __name__ == '__main__':
    unittest.main()
