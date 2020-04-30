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


def write_tables_2_file(tables_str: list, header_words: list, step: int, output_file: str = 'out.txt') -> None:
  """Write to default out.txt file tables listed separated by means of two blank lines"""
  for ii, table in enumerate(tables_str):
    with open('out.txt'.format(str(ii)), "a") as f:
      print('write table on file...')
      f.write('\n')
      f.write('\n')
      hw = header_words[ii*step:(ii+1)*step]
      res = ' & '.join([xi for xi in hw]) 
      f.write(res + ' \\\\\n')
      f.write('\\hline\n')
      f.writelines(table)
      pass
    pass
  pass