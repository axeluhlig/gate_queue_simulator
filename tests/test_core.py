import unittest
import context

from simulator import core as unit


class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.flakiness = 0.01
        self.unit = unit.Simulator()

    def __chances_for_no_gate_reset_at_given_queue_position(self, queue_position, expected_value):
        actual_value = self.unit.get_chances_for_no_gate_reset_at_any_element_in_queue_until_given_index(
            self.flakiness, queue_position)
        self.assertEqual(expected_value, actual_value)

    def test_chances_for_no_gate_reset_at_queue_position_0(self):
        self.__chances_for_no_gate_reset_at_given_queue_position(
            0, 1 - self.flakiness)

    def test_chances_for_no_gate_reset_at_queue_position_1(self):
        self.__chances_for_no_gate_reset_at_given_queue_position(
            1,  (1 - self.flakiness) * (1- self.flakiness))

    def test_chances_for_no_gate_reset_at_queue_position_10(self):
        self.__chances_for_no_gate_reset_at_given_queue_position(
            10, pow(1 - self.flakiness, 11))

    def test_chances_for_no_gate_reset_at_queue_position_99(self):
        self.__chances_for_no_gate_reset_at_given_queue_position(
            99, pow(1 - self.flakiness, 100))


if __name__ == '__main__':
    unittest.main()
