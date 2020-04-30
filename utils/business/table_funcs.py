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
  
  with open('out.txt', "w") as f:
    for ii, table in enumerate(tables_str):
      # print('write table on file...')
      
      
      f.write('\n')
      f.write('\n')

      f.write('\\begin{center}')
      f.write('\\begin{tabular}{ |' + 'c|' * step + '}')
      f.write('\\hline\n')
      
      f.write('\\multicolumn{%d}{|c|}{\\textbf{Synonims - Tab no.??}} \\\\' % (step, ))
      f.write('\\hline\n')
      # Header
      hw = header_words[ii*step:(ii+1)*step]
      res = ' & '.join([xi for xi in hw]) 
      f.write(res + ' \\\\\n')

      # Content
      f.write('\\hline\n')
      f.writelines(table)
      f.write('\\hline\n')

      f.write('\\end{tabular}')
      f.write('\\end{center}')
      pass
    pass
  pass