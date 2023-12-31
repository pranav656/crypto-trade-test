
from abc import ABC, abstractmethod
from collections import deque
import pandas as pd

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

class SimpleMovingAverageStrategy(BaseStrategy):
    def __init__(self, prices, window):
        self.prices = prices
        self.window = window
        # Signal indicates a moving average crossover
        self.signals = None
    
    def calculate_signals(self):
        self.moving_average=self.prices.rolling(window=self.window).mean()
        print(self.moving_average)
    
    #TODO
    def execute_trades(self):
        return super().execute_trades()
    
    def run_strategy(self):
        self.calculate_signals()
        self.execute_trades()

# create a FIFO queue and push dummy data into it
fifo_queue = FixedLengthFifo(50)
for i in range(0, 50):
    fifo_queue.push(i)

# test strategy for 20 datapoints
df = pd.DataFrame(list(fifo_queue.queue))
strategy = SimpleMovingAverageStrategy(df, 20)
strategy.calculate_signals()