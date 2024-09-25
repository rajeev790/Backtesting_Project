import unittest
from utils.data_loader import load_data

class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        data = load_data('data/Nifty/expiry_2023_01_25.feather')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
