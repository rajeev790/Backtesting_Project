import logging
import os

def setup_logging(log_file='backtesting.log', log_level=logging.INFO):
    """Sets up logging configuration for the backtesting project."""
    
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configure logging settings
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(f'logs/{log_file}'),
            logging.StreamHandler()
        ]
    )
    
    logging.getLogger('matplotlib').setLevel(logging.WARNING)  # Avoid unnecessary logging from matplotlib
    logging.getLogger('backtest').info("Logging initialized.")

# Example usage
if __name__ == "__main__":
    setup_logging()
