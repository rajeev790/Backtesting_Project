import numpy as np

class PerformanceMetrics:
    def __init__(self, returns):
        """
        Initialize with the returns from the backtest.
        :param returns: A list or numpy array of percentage returns for each trade
        """
        self.returns = np.array(returns)

    def calculate_sharpe_ratio(self, risk_free_rate=0):
        """
        Calculate the Sharpe ratio.
        :param risk_free_rate: The risk-free rate for excess return calculation
        :return: Sharpe ratio
        """
        excess_returns = self.returns - risk_free_rate
        return np.mean(excess_returns) / np.std(excess_returns)

    def calculate_drawdown(self):
        """
        Calculate the maximum drawdown.
        :return: Maximum drawdown value
        """
        cumulative_returns = np.cumsum(self.returns)
        peak = np.maximum.accumulate(cumulative_returns)
        drawdown = cumulative_returns - peak
        max_drawdown = np.min(drawdown)
        return max_drawdown
