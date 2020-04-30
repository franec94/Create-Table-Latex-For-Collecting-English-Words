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

# Custom imports
from utils.business import table_funcs


# ------------------------------------------------------------- #
# Read input data
# ------------------------------------------------------------- #

def read_input_data(input_files: list = ['input.txt']) -> str:

  print('Read input data...')
  all_val: str = ''
  for a_file in input_files:
    with open(a_file) as f:
      val: str = f.read()
      all_val += val
  return all_val


# ------------------------------------------------------------- #
# Prepare, Preprocess input data
# ------------------------------------------------------------- #

def _padd(item: list, max_len: int) -> list:
  delta = max_len - len(item)
  if delta != 0:
    item = item + [''] * delta
  return item

def prepare_preprocess_input_data(val) -> object:

  print('Preprocess input data...')
  # From text corpus to list of list of strings
  res = val.split('\n')
  res = filter(lambda xi: len(xi) > 0, res)
  res = list(res)

  # Divide words of a language to words of another
  # where the formers are well known, whereas the latters are target.
  knwon_words = list(map(str.capitalize, res[0:-1:2]))
  target_words = res[1::2]

  msg_assert: str = 'len(target_words) == len(knwon_words different lenghts, acctualli former=%d, latter%d' % (len(target_words), len(knwon_words))
  assert len(target_words) == len(knwon_words), msg_assert

  target_words = map(lambda xi: xi.strip().split(','), target_words)
  target_words = list(target_words)

  max_len = max(
    list(
      map(lambda xi: len(xi), target_words)
    )
  )

  target_words = list(
    map(lambda xi: _padd(xi, max_len), target_words)
  )

  def bold_it(item):
    return '\\textbf{' + item + '}'
  knwon_words = list(map(bold_it, knwon_words))

  return target_words, knwon_words, max_len

# ------------------------------------------------------------- #
# Process, produce output, result data
# ------------------------------------------------------------- #

def _check_input_data_process_data(input_data, input_names) -> None:

  print('Process input data...')
  for name, val in zip(input_names, input_data):
    assert val != None, f'{name} is None'
  
  # data_int = filter(lambda xi: type(xi) is int, input_data)
  index_data_int = filter(lambda xi: type(xi[1]) is int, enumerate(input_data))

  for index, val in index_data_int:
    assert val > 0, f'{input_names[index]} is negative or zeroed, acctually: {val}'
  pass

def process_data(target_words: list, step: int, max_len: int) -> list:

  input_data = [target_words, step, max_len]
  input_names = ['target_words', 'step', 'max_len']

  _check_input_data_process_data(input_data, input_names)

  tables = list()
  for ii in range(0, len(target_words), step):
    # print('Procesing sublock no.{}'.format(ii))
    val = list()
    for jj in range(max_len):
      # print(jj)
      res = list()
      for zz in range(step):
        # print(zz)
        res.append(target_words[zz+ii][jj])
      val.append(res)
    tables.append(val)

  tables_str = list()
  for table in tables:
    # print('Processing...')
    table_str = list()
    lens = list()
    for ii in range(step):
      # print(table[0:-1][ii])
      res = max(map(len, table[0:-1][ii]))
      lens.append(res)
    l = list()
    for xx in lens:
      l.append('%{}s'.format(xx))
    res_x = ' & '.join([xi for xi in l])
    # print(res_x)
    for row in table:
      res = ' & '.join([xi for xi in row])
      # print(tuple(row))
      # res = copy.deepcopy(res_x) % tuple(row)
      table_str.append(res + ' \\\\\n')
    tables_str.append(table_str)
    # pprint(table_str)
  return tables_str


# ------------------------------------------------------------- #
# Write results as output data
# ------------------------------------------------------------- #

def write_results(results: list, header_items: list, step):
  print('Wrtie output data...')
  table_funcs.write_tables_2_file(results, header_items, step)
  pass

# ------------------------------------------------------------- #
# Prepare, Preprocess input data (Backup)
# ------------------------------------------------------------- #

def _prepare_preprocess_input_data_backup(val) -> object:

  # From text corpus to list of list of strings
  res = val.split('\n')
  res = filter(lambda xi: len(xi) > 0, res)
  res = list(res)

  # Divide words of a language to words of another
  # where the formers are well known, whereas the latters are target.
  knwon_words = list(map(str.capitalize, res[0:-1:2]))
  target_words = res[1::2]

  msg_assert: str = 'len(target_words) == len(knwon_words different lenghts, acctualli former=%d, latter%d' % (len(target_words), len(knwon_words))
  assert len(target_words) == len(knwon_words), msg_assert

  target_words = map(lambda xi: xi.strip().split(','), target_words)
  target_words = list(target_words)

  max_len = max(
    list(
      map(lambda xi: len(xi), target_words)
    )
  )

  target_words = list(
    map(lambda xi: _padd(xi, max_len), target_words)
  )
  val = list()
  for ii in range(max_len):
    res = list()
    for jj in range(len(knwon_words)):
      # print(english_words[jj][ii])
      res.append(target_words[jj][ii])
    res = ' & '.join([xi for xi in res])
    val.append(' & ' + res + ' \\\\\n')

  # pprint(val)
  with open('out.txt', "w") as f:
    f.writelines(val)
  # ------------------------------------------------------------- #
  print(max_len)
  print(knwon_words)
  def bold_it(item):
    return '\\textbf{' + item + '}'
  knwon_words = list(map(bold_it, knwon_words))

  val = list()
  for ii in range(max_len):
    res = list()
    for jj in range(len(knwon_words)):
      # print(english_words[jj][ii])
      res.append(target_words[jj][ii])
    val.append(res)
  return target_words, knwon_words, max_len