
from abc import ABC, abstractmethod
from collections import deque
import pandas as pd
   
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
    def __init__(self, data, window):
        self.data = data
        self.window = window
        # Signal indicates a moving average crossover
        self.signal = None

    def update_data(self, new_data):
        self.data = pd.concat([self.data, new_data])
    
    def calculate_signals(self):
        latest_ma = self.data['Close'].rolling(window=self.window).mean().iloc[-1]
        self.signal = True if(self.data['Close'].iloc[-1] > latest_ma) else False
        
    def execute_trades(self):
        print("BUY") if self.signal else print("SELL")
    
    def run_strategy(self):
        self.calculate_signals()
        self.execute_trades()

# create a list and push dummy data into it
start_price_data = {
    'Date': pd.date_range(start='2023-01-01', periods=100),
    'Close': [189 + i for i in range(100)]
}

# test strategy for dummy data points based on 20 point
# moving average, sells on a dowanard trend and buys on
# an upward trend
df = pd.DataFrame(start_price_data)
strategy = SimpleMovingAverageStrategy(df, 20)
strategy.calculate_signals()

for i in range(100):
    dummy_current_data = {
        'Date': pd.date_range(start='2023-01-01', periods=1),
        'Close': [95+i]
    }
    strategy.update_data(pd.DataFrame(dummy_current_data))
    strategy.calculate_signals()
    strategy.execute_trades()
