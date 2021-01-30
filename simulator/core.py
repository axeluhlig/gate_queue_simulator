from random import choices, randrange


class Simulator:

    def get_chances_for_no_gate_reset_at_any_element_in_queue_until_given_index(self, flakiness, index):
        return pow(1-flakiness, index + 1)

    def do_basic_sim(self, initial_queue_length, flakiness, new_elements_per_time_interval, duration, verbosity=True):
        # this basic sim assumes that all elements in the queue start their checks at the same time and that they take all exactly the same time. New elements are only added after the end of a cycle.
        queue_length = initial_queue_length
        if verbosity:
            print('t', 'gate_reset', 'queue_length', 'chances_for_gate_reset')
        for t in list(range(duration)):
            # does a gate reset happen?
            chances_for_no_gate_reset_at_current_queue_length = self.get_chances_for_no_gate_reset_at_any_element_in_queue_until_given_index(
                flakiness, queue_length)
            gate_reset = choices([True, False], [
                                 1-chances_for_no_gate_reset_at_current_queue_length, chances_for_no_gate_reset_at_current_queue_length])[0]
            # where in the queue
            if gate_reset:
                # the position of the gate reset is completetly random (in this very simple simulator), therefore a random number of elements remain in the queue (all elements after the gate reset position)
                queue_length = randrange(0, queue_length)
            else:
                queue_length = 0  # given the assumptions of this basic sim, all elements are done
            if verbosity:
                print(t, gate_reset, queue_length,
                      chances_for_no_gate_reset_at_current_queue_length)
            queue_length += new_elements_per_time_interval
        return queue_length
