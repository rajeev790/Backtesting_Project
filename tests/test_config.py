import unittest
from utils.config import get_config_value

class TestConfig(unittest.TestCase):

    def test_get_config_value(self):
        value = get_config_value('data_directory')
        self.assertEqual(value, 'data/')

if __name__ == '__main__':
    unittest.main()
