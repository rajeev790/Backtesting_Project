from datetime import datetime

class DateUtils:
    @staticmethod
    def str_to_date(date_str, date_format='%Y-%m-%d'):
        """
        Convert a date string to a datetime object.
        :param date_str: Date in string format
        :param date_format: The format of the date string (default: 'YYYY-MM-DD')
        :return: Datetime object
        """
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError as e:
            print(f"Error parsing date: {e}")
            return None

    @staticmethod
    def date_to_str(date_obj, date_format='%Y-%m-%d'):
        """
        Convert a datetime object to a formatted string.
        :param date_obj: Datetime object
        :param date_format: Desired string format (default: 'YYYY-MM-DD')
        :return: Date string
        """
        return date_obj.strftime(date_format)
