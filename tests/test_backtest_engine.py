import unittest
from backtest.backtest_engine import BacktestEngine

class TestBacktestEngine(unittest.TestCase):

    def test_run_backtest(self):
        engine = BacktestEngine(strategy='ma_crossover', initial_balance=100000)
        results = engine.run_backtest()
        self.assertIsNotNone(results)
        self.assertGreater(results['final_balance'], 0)

if __name__ == '__main__':
    unittest.main()
