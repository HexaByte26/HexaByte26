# Toll Gate

class TollGate:
    def __init__(self, max_size):
        "param:"
        "   max_size - max size of the queue"
        self.toll_queue_max_size = max_size
        self.toll_queue = ["___"] * self.toll_queue_max_size
        self.toll_rear = -1
        self.toll_front = -1
        self.toll_queue_count = 0

    def is_empty(self):
        return self.toll_queue_count == 0
    
    def is_full(self):
        return self.toll_queue_count == self.toll_queue_max_size
    
    def enqueue_vehicle(self, vehicle):
        