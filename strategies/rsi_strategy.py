import pandas as pd
from strategy_base import StrategyBase

class RSIStrategy(StrategyBase):
    def __init__(self, data, rsi_window=14, overbought=70, oversold=30):
        super().__init__(data)
        self.rsi_window = rsi_window
        self.overbought = overbought
        self.oversold = oversold

    def calculate_rsi(self):
        delta = self.data['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        avg_gain = gain.rolling(window=self.rsi_window).mean()
        avg_loss = loss.rolling(window=self.rsi_window).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def generate_signals(self):
        self.data['RSI'] = self.calculate_rsi()
        
        for i in range(len(self.data)):
            if self.data['RSI'].iloc[i] < self.oversold:
                if self.position != "long":
                    if self.position == "short":
                        self.close_position(self.data['Close'].iloc[i])
                    self.open_position(self.data['Close'].iloc[i], "long")
            elif self.data['RSI'].iloc[i] > self.overbought:
                if self.position != "short":
                    if self.position == "long":
                        self.close_position(self.data['Close'].iloc[i])
                    self.open_position(self.data['Close'].iloc[i], "short")
