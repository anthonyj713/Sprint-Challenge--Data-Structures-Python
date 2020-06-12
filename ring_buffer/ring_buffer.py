class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.list = [None] * capacity

    def append(self, item):
        if self.count >= self.capacity:
            self.count = 0
        self.list[self.count] = item
        self.count += 1
      
    def get(self):
        return [item for item in self.list if item is not None]