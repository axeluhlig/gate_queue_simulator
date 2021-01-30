class Simulator:

    def __init__(self, flakiness, max_queue_length=100):
        # flakiness: in percent
        self.chances_for_no_gate_reset_at_any_element_in_queue_until_given_index = []
        # the index is the position in the queue
        for i in range(max_queue_length):
            self.chances_for_no_gate_reset_at_any_element_in_queue_until_given_index.append(
                pow(flakiness, i+1))
