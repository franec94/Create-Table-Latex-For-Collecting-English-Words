print(__doc__)

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

# Custom imports
from utils.business import work 


# ------------------------------------------------------------- #
# Main function
# ------------------------------------------------------------- #

def main() -> None:
  # ------------------------------------------------------------- #
  # Read input data
  # ------------------------------------------------------------- #
  val = work.read_input_data()

  # ------------------------------------------------------------- #
  # Prepare, Preprocess input data
  # ------------------------------------------------------------- #
  target_words, knwon_words, max_len = \
    work.prepare_preprocess_input_data(val)

  # ------------------------------------------------------------- #
  # Process, produce output, result data
  # ------------------------------------------------------------- #
  tables = work.process_data(
    target_words=target_words,
    step=4)

  # ------------------------------------------------------------- #
  # Write results as output data
  # ------------------------------------------------------------- #
  work.write_results(
    results=tables,
    header_items=knwon_words)
  pass


# ------------------------------------------------------------- #
# Entry Point
# ------------------------------------------------------------- #
if __name__ == '__main__':

  # ------------------------------------------------------------- #
  # Main function: it starts work...
  # ------------------------------------------------------------- #
  main()
  pass