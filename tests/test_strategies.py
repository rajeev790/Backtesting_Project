import unittest
from strategies.ma_crossover import MovingAverageCrossover
from strategies.rsi_strategy import RSIStrategy

class TestStrategies(unittest.TestCase):

    def test_ma_crossover(self):
        ma_crossover = MovingAverageCrossover(short_window=5, long_window=10)
        signal = ma_crossover.generate_signal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertIn(signal, ['buy', 'sell', 'hold'])

    def test_rsi_strategy(self):
        rsi = RSIStrategy(period=14)
        signal = rsi.generate_signal([30, 70, 50, 80, 40])
        self.assertIn(signal, ['buy', 'sell', 'hold'])

if __name__ == '__main__':
    unittest.main()
