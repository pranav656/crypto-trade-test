
from abc import ABC, abstractmethod
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
