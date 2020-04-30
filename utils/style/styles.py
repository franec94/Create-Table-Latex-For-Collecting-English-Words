print('File name: ' + __name__ + ', doc string: ', __doc__, sep='\n')

# ------------------------------------------------------------- #
# Packages, Libraries, Imports
# ------------------------------------------------------------- #

from pprint import pprint

import copy
import datetime
import json
import os
import sys
import time
import yaml


def bold_it(item: str) -> str:
  """Takes an input string and returns an output string in the following manner:
      return '\\textbf{' + item + '}' that stands for bold version of item."""
  return '\\textbf{' + item + '}'


def italic_it(item: str) -> str:
  """Takes an input string and returns an output string in the following manner:
      return '\\textit{' + item + '}' that stands for italic version of item."""
  return '\\textit{' + item + '}'