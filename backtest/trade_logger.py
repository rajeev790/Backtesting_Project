class TradeLogger:
    def __init__(self):
        """
        Initialize an empty trade log.
        """
        self.trades = []
    
    def log_trade(self, position, entry_price, exit_price, date):
        """
        Log a trade to the trade history.
        :param position: "long" or "short"
        :param entry_price: Price at which the position was entered
        :param exit_price: Price at which the position was exited
        :param date: The date of the trade exit
        """
        trade = {
            'Position': position,
            'Entry Price': entry_price,
            'Exit Price': exit_price,
            'Exit Date': date,
            'P/L': (exit_price - entry_price) if position == 'long' else (entry_price - exit_price)
        }
        self.trades.append(trade)

    def display_trade_log(self):
        """
        Display the full trade log after backtesting.
        """
        print("Trade Log:")
        for trade in self.trades:
            print(f"{trade['Position']} position, Entry: {trade['Entry Price']}, Exit: {trade['Exit Price']}, "
                  f"Exit Date: {trade['Exit Date']}, P/L: {trade['P/L']}")
