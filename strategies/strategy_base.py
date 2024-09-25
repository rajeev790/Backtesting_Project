class StrategyBase:
    def __init__(self, data, initial_balance=100000):
        """
        Base class for all strategies.
        :param data: Historical data (Pandas DataFrame)
        :param initial_balance: Initial account balance for backtesting
        """
        self.data = data
        self.balance = initial_balance
        self.position = 0  # Long or Short
        self.entry_price = None
        self.exit_price = None
        self.profit_loss = 0
        self.trade_history = []
    
    def open_position(self, price, position_type):
        """
        Open a new position.
        :param price: Entry price
        :param position_type: "long" or "short"
        """
        self.position = position_type
        self.entry_price = price
        print(f"Opening {position_type} position at {price}")

    def close_position(self, price):
        """
        Close the current position.
        :param price: Exit price
        """
        if self.position == "long":
            self.profit_loss += price - self.entry_price
        elif self.position == "short":
            self.profit_loss += self.entry_price - price
        self.trade_history.append((self.position, self.entry_price, price))
        print(f"Closing {self.position} position at {price}. P/L: {self.profit_loss}")
        self.position = 0
        self.entry_price = None

    def generate_signals(self):
        """
        To be implemented by specific strategies.
        """
        raise NotImplementedError("generate_signals must be implemented by the strategy.")
