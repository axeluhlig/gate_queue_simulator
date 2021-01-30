from random import choices, randrange


class Simulator:

    def get_chances_for_no_gate_reset_at_any_element_in_queue_until_given_index(self, flakiness, index):
        return pow(1-flakiness, index + 1)

    def do_basic_sim(self, flakiness, new_elements_per_time_interval, cycle, verbosity=True):
        # Assumptions for this basic sim:
        # - all elements in the queue start their checks at the same time
        # - all elements take the same amount of time
        # - the gate reset always happens at the head of the queue
        # - new elements are only added after the end of a cycle.
        queue_length = 0
        queue_length_over_time = []
        if verbosity:
            print('t', 'gate_reset', 'queue_length', 'chances_for_gate_reset')
        for t in list(range(cycle)):
            queue_length += new_elements_per_time_interval
            # does a gate reset happen?
            chances_for_no_gate_reset_at_current_queue_length = self.get_chances_for_no_gate_reset_at_any_element_in_queue_until_given_index(
                flakiness, queue_length)
            gate_reset = choices([True, False], [
                                 1-chances_for_no_gate_reset_at_current_queue_length, chances_for_no_gate_reset_at_current_queue_length])[0]
            # where in the queue
            if gate_reset:
                queue_length -= 1  # given the assumptions of this basic sim, only the head is removed
            else:
                queue_length = 0  # given the assumptions above all elements can be removed
            if verbosity:
                print(t, gate_reset, queue_length,
                      chances_for_no_gate_reset_at_current_queue_length)
            queue_length_over_time.append(queue_length)
        return queue_length_over_time
