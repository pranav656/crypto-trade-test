
from abc import ABC, abstractmethod
from bfxapi.types import Candle
from collections import deque

class FixedLengthFifo:
    def __init__(self, max_length):
        self.queue = deque(maxlen=max_length)

    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty queue")
    
    def __len__(self):
        return len(self.queue)
    
class BaseStrategy(ABC):
    @abstractmethod
    def calculate_signals(self):
        pass
    
    @abstractmethod
    def execute_trades(self):
        pass

    @abstractmethod
    def run_strategy(self):
        pass

c = Candle(10102024, 2, 3, 4, 5, 6.0)