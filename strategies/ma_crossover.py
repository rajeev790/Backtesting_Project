import pandas as pd
from strategy_base import StrategyBase

class MovingAverageCrossover(StrategyBase):
    def __init__(self, data, short_window=50, long_window=200):
        super().__init__(data)
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        self.data['short_ma'] = self.data['Close'].rolling(window=self.short_window).mean()
        self.data['long_ma'] = self.data['Close'].rolling(window=self.long_window).mean()
        
        for i in range(len(self.data)):
            if self.data['short_ma'].iloc[i] > self.data['long_ma'].iloc[i]:
                if self.position != "long":
                    if self.position == "short":
                        self.close_position(self.data['Close'].iloc[i])
                    self.open_position(self.data['Close'].iloc[i], "long")
            elif self.data['short_ma'].iloc[i] < self.data['long_ma'].iloc[i]:
                if self.position != "short":
                    if self.position == "long":
                        self.close_position(self.data['Close'].iloc[i])
                    self.open_position(self.data['Close'].iloc[i], "short")
