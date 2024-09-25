import pandas as pd
from trade_logger import TradeLogger

class BacktestEngine:
    def __init__(self, strategy, data):
        """
        Initialize the backtest engine with the strategy and historical data.
        :param strategy: The trading strategy to apply (instance of StrategyBase)
        :param data: Historical data (Pandas DataFrame)
        """
        self.strategy = strategy
        self.data = data
        self.trade_logger = TradeLogger()
    
    def run(self):
        """
        Execute the backtest by applying the strategy to the historical data.
        """
        print("Starting backtest...")
        self.strategy.generate_signals()
        
        for i, row in self.data.iterrows():
            # Handle position opening/closing based on the strategy
            if self.strategy.position != 0:
                self.trade_logger.log_trade(self.strategy.position, self.strategy.entry_price, row['Close'], row['Date'])
        
        print(f"Final P/L: {self.strategy.profit_loss}")
        self.trade_logger.display_trade_log()
