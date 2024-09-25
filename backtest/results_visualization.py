import matplotlib.pyplot as plt

class ResultsVisualization:
    def __init__(self, equity_curve):
        """
        Initialize with the equity curve data.
        :param equity_curve: A list or array of cumulative equity values over the backtest period
        """
        self.equity_curve = equity_curve

    def plot_equity_curve(self):
        """
        Plot the equity curve to visualize the account balance over time.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(self.equity_curve, label='Equity Curve', color='blue')
        plt.title('Equity Curve')
        plt.xlabel('Time')
        plt.ylabel('Account Balance')
        plt.legend()
        plt.grid()
        plt.show()

    def plot_drawdown(self, drawdown):
        """
        Plot the drawdown over time.
        :param drawdown: A list or array of drawdown values over time
        """
        plt.figure(figsize=(10, 6))
        plt.plot(drawdown, label='Drawdown', color='red')
        plt.title('Drawdown')
        plt.xlabel('Time')
        plt.ylabel('Drawdown Value')
        plt.legend()
        plt.grid()
        plt.show()
