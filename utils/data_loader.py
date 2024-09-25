import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        """
        Initialize the DataLoader with the file path.
        :param file_path: Path to the historical data file
        """
        self.file_path = file_path

    def load_data(self):
        """
        Load historical data from the file.
        :return: Pandas DataFrame containing the historical data
        """
        try:
            if self.file_path.endswith('.feather'):
                data = pd.read_feather(self.file_path)
            elif self.file_path.endswith('.csv'):
                data = pd.read_csv(self.file_path)
            elif self.file_path.endswith('.parquet'):
                data = pd.read_parquet(self.file_path)
            else:
                raise ValueError("Unsupported file format. Use Feather, CSV, or Parquet.")
            return data
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
