import pandas as pd
from strategy_base import StrategyBase

class BollingerBandsStrategy(StrategyBase):
    def __init__(self, data, window=20, std_dev=2):
        super().__init__(data)
        self.window = window
        self.std_dev = std_dev

    def generate_signals(self):
        self.data['MA'] = self.data['Close'].rolling(window=self.window).mean()
        self.data['Upper_Band'] = self.data['MA'] + (self.data['Close'].rolling(window=self.window).std() * self.std_dev)
        self.data['Lower_Band'] = self.data['MA'] - (self.data['Close'].rolling(window=self.window).std() * self.std_dev)
        
        for i in range(len(self.data)):
            if self.data['Close'].iloc[i] < self.data['Lower_Band'].iloc[i]:
                if self.position != "long":
                    if self.position == "short":
                        self.close_position(self.data['Close'].iloc[i])
                    self.open_position(self.data['Close'].iloc[i], "long")
            elif self.data['Close'].iloc[i] > self.data['Upper_Band'].iloc[i]:
                if self.position != "short":
                    if self.position == "long":
                        self.close_position(self.data['Close'].iloc[i])
                    self.open_position(self.data['Close'].iloc[i], "short")
