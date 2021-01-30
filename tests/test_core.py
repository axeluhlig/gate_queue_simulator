import unittest
import context

from simulator import core as unit


class TestSimulator(unittest.TestCase):

    def setUp(self):
        self.unit = unit.Simulator()

    def __chances_for_no_gate_reset_at_given_queue_position(self, queue_position, expected_value, flakiness):
        actual_value = self.unit.get_chances_for_no_gate_reset_at_any_element_in_queue_until_given_index(
            flakiness, queue_position)
        self.assertEqual(expected_value, actual_value)

    def test_chances_for_no_gate_reset_at_queue_position_0(self):
        flakiness = 0.01
        expected_value = 1 - flakiness

        self.__chances_for_no_gate_reset_at_given_queue_position(
            0, expected_value, flakiness)

    def test_chances_for_no_gate_reset_at_queue_position_1(self):
        flakiness = 0.01
        expected_value = (1 - flakiness) * (1 - flakiness)

        self.__chances_for_no_gate_reset_at_given_queue_position(
            1, expected_value, flakiness)

    def test_chances_for_no_gate_reset_at_queue_position_10(self):
        flakiness = 0.01
        expected_value = pow(1 - flakiness, 11)

        self.__chances_for_no_gate_reset_at_given_queue_position(
            10, expected_value, flakiness)

    def test_chances_for_no_gate_reset_at_queue_position_99(self):
        flakiness = 0.01
        expected_value = pow(1 - flakiness, 100)

        self.__chances_for_no_gate_reset_at_given_queue_position(
            99, expected_value, flakiness)

    def test_chances_for_no_gate_reset_at_for_red_gate(self):
        flakiness = 1
        expected_value = 0.0
        position = 1

        self.__chances_for_no_gate_reset_at_given_queue_position(
            position, expected_value, flakiness)

    def test_basic_sim_red_gate(self):
        flakiness = 1.0
        new_elements_per_time_interval = 10
        cycle = 10
        expected__final_queue_length = cycle * new_elements_per_time_interval - \
            cycle  # total number of elements added - number of elements removed because of gate reset

        resulting_queue_length = self.unit.do_basic_sim(
            flakiness, new_elements_per_time_interval, cycle, verbosity=False)

        self.assertEqual(expected__final_queue_length,
                         resulting_queue_length[-1])


if __name__ == '__main__':
    unittest.main()
