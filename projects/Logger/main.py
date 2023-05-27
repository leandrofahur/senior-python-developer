from os import path, makedirs
from enum import Enum
from datetime import datetime


class Log_Level(Enum):
  INFO = 0
  WARNING = 1
  ERROR = 2
  CRITICAL = 3


class Logger:
  """
  This is a basic Logger class that can be used to log messages to a file.
  """

  def __init__(self, log_dir=path.abspath('./logs')):
    """
    Initialize the logger with a log level and file name.
    :param log_dir: The folder directory created by default: ./logs.
    """
    self._filename = datetime.now().strftime('%Y%m%d%H%M%S')

    # Create logs directory if it doesn't exist.
    makedirs('./logs', exist_ok=True)

    self._file = path.join(log_dir, f'{self._filename}.txt')

    with open(self._file, 'w', encoding='utf-8') as f:
      f.write(f'{datetime.now()}:\n')

  def info(self, message: str, log_level=Log_Level.INFO):
    """
    Write an info message to the log file.
    :param message: The info message.
    :param log_level: The log_level INFO
    """
    with open(self._file, 'a', encoding='utf-8') as f:
      f.write(
          f'[{log_level.INFO.name}] - {datetime.now().strftime("%H:%M:%S")}: {message}\n')

  def warning(self, message: str, log_level=Log_Level.WARNING):
    """
    Write an warning message to the log file.
    :param message: The warning message.
    :param log_level: The log_level WARNING
    """
    with open(self._file, 'a', encoding='utf-8') as f:
      f.write(
          f'[{log_level.WARNING.name}] - {datetime.now().strftime("%H:%M:%S")}: {message}\n')

  def error(self, message: str, log_level=Log_Level.ERROR):
    """
    Write an error message to the log file.
    :param message: The error message.
    :param log_level: The log_level ERROR
    """
    with open(self._file, 'a', encoding='utf-8') as f:
      f.write(
          f'[{log_level.ERROR.name}] - {datetime.now().strftime("%H:%M:%S")}: {message}\n')

  def critical(self, message: str, log_level=Log_Level.ERROR):
    """
    Write an critical message to the log file.
    :param message: The critical message.
    :param log_level: The log_level CRITICAL
    """
    with open(self._file, 'a', encoding='utf-8') as f:
      f.write(
          f'[{log_level.CRITICAL.name}] - {datetime.now().strftime("%H:%M:%S")}: {message}\n')


logger = Logger()
print(logger.info.__doc__)
logger.info("Loggingmy first information")
logger.error("Loggingmy first error")
