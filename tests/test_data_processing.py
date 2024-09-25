import unittest
from utils.data_processing import process_data

class TestDataProcessing(unittest.TestCase):

    def test_process_data(self):
        raw_data = [1, 2, 3, 4, 5]
        result = process_data(raw_data)
        self.assertEqual(result, [1, 2, 3, 4, 5])  # Modify according to actual processing logic

if __name__ == '__main__':
    unittest.main()
