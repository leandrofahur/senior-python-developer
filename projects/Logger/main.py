""""
This is a basic Logger class that can be used to log messages to a file.
"""

from os import path, makedirs
from enum import Enum
from datetime import datetime


class Log_Level(Enum):
  DEBUG = 0
  INFO = 1
  WARNING = 2
  ERROR = 3
  CRITICAL = 4


class Logger:
  def __init__(self):
    self._filename = datetime.now().strftime('%Y%m%d%H%M%S')

    # Create logs directory if it doesn't exist
    makedirs('./logs', exist_ok=True)

    self._file = path.join('./logs', f'{self._filename}.txt')

    with open(self._file, 'w', encoding='utf-8') as f:
      f.write(f'{datetime.now()}:\n')


logger = Logger()
