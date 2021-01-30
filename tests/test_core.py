import unittest
import context

from simulator import core as unit


class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.flakiness = 0.01
        self.unit = unit.Simulator(self.flakiness)

    def test_chances_for_no_gate_reset_at_queue_position_0(self):
        expected_value = self.flakiness

        actual_value = self.unit.chances_for_no_gate_reset_at_any_element_in_queue[0]

        self.assertEqual(expected_value, actual_value)


if __name__ == '__main__':
    unittest.main()
