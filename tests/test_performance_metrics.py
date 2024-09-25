import unittest
from backtest.performance_metrics import calculate_sharpe_ratio

class TestPerformanceMetrics(unittest.TestCase):

    def test_calculate_sharpe_ratio(self):
        returns = [0.02, 0.03, 0.01, -0.01, 0.04]
        sharpe_ratio = calculate_sharpe_ratio(returns, risk_free_rate=0.01)
        self.assertGreater(sharpe_ratio, 0)

if __name__ == '__main__':
    unittest.main()
