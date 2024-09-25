import os
import logging
import yaml
from utils.data_loader import load_historical_data
from backtest.backtest_engine import BacktestEngine
from strategies.ma_crossover import MovingAverageCrossover
from strategies.rsi_strategy import RSI
from utils.logger import setup_logger
from config.config import load_config

def main():
    # Setup logging
    setup_logger()
    logger = logging.getLogger(__name__)

    # Load configuration
    config = load_config("config/config.yaml")
    logger.info("Configuration loaded successfully.")

    # Load historical data
    logger.info("Loading historical data...")
    data = load_historical_data(config['data_directory'])
    logger.info("Historical data loaded successfully.")

    # Initialize the backtest engine
    backtest_engine = BacktestEngine(data)

    # Define strategies based on configuration
    strategies = []
    if "ma_crossover" in config['strategies']:
        ma_strategy = MovingAverageCrossover(config['strategy_params']['ma_crossover'])
        strategies.append(ma_strategy)
        logger.info("Moving Average Crossover strategy added.")

    if "rsi" in config['strategies']:
        rsi_strategy = RSI(config['strategy_params']['rsi'])
        strategies.append(rsi_strategy)
        logger.info("RSI strategy added.")

    # Run backtesting for each strategy
    for strategy in strategies:
        logger.info(f"Running backtest for strategy: {strategy.__class__.__name__}")
        results = backtest_engine.run_backtest(strategy)
        
        # Save results
        logger.info("Saving results...")
        backtest_engine.save_results(results, strategy.__class__.__name__)
        logger.info(f"Results saved for strategy: {strategy.__class__.__name__}")

    logger.info("Backtesting completed successfully.")

if __name__ == "__main__":
    main()
