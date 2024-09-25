import pandas as pd

class DataProcessing:
    @staticmethod
    def filter_data(data, start_date, end_date):
        """
        Filter the historical data between start_date and end_date.
        :param data: Pandas DataFrame containing historical data
        :param start_date: The start date for filtering (inclusive)
        :param end_date: The end date for filtering (inclusive)
        :return: Filtered DataFrame
        """
        filtered_data = data[(data['Date'] >= start_date) & (data['Date'] <= end_date)]
        return filtered_data

    @staticmethod
    def load_in_chunks(file_path, chunk_size=10000):
        """
        Load large datasets in chunks.
        :param file_path: Path to the file
        :param chunk_size: Number of rows per chunk
        :return: Generator yielding chunks of data
        """
        try:
            for chunk in pd.read_csv(file_path, chunksize=chunk_size):
                yield chunk
        except Exception as e:
            print(f"Error loading data in chunks: {e}")
            return None
