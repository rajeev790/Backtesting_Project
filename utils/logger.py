import logging

class Logger:
    @staticmethod
    def setup_logger(name, log_file, level=logging.INFO):
        """
        Set up a logger for debugging and tracking.
        :param name: The name of the logger
        :param log_file: File path for saving the logs
        :param level: Logging level (default: INFO)
        :return: Configured logger instance
        """
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger
