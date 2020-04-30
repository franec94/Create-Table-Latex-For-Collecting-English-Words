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


# ------------------------------------------------------------- #
# Prepare, Preprocess input data
# ------------------------------------------------------------- #

# From text corpus to list of list of strings
res = val.split('\n')
res = filter(lambda xi: len(xi) > 0, res)
res = list(res)

# Divide words of a language to words of another
# where the formers are well known, whereas the latters are target.
knwon_words = list(map(str.capitalize, res[0:-1:2]))
target_words = res[1::2]

msg_assert: str = 'len(italian_words) == len(english_words different lenghts'
assert len(target_words) == len(knwon_words), msg_assert

english_words = map(lambda xi: xi.strip().split(','), target_words)
english_words = list(english_words)

max_len = max(
  list(
    map(lambda xi: len(xi), english_words)
    )
    )


def padd(item, max_len):
  delta = max_len - len(item)
  if delta != 0:
    item = item + [''] * delta
  return item

english_words = list(
    map(lambda xi: padd(xi, max_len), english_words)
    )

from pprint import pprint
# pprint(english_words)

val = list()
for ii in range(max_len):
  res = list()
  for jj in range(len(knwon_words)):
    # print(english_words[jj][ii])
    res.append(english_words[jj][ii])
  res = ' & '.join([xi for xi in res])
  val.append(' & ' + res + ' \\\\\n')

pprint(val)
with open('out.txt', "w") as f:
  f.writelines(val)

# ------------------------------------------------------------- #
print(max_len)
print(knwon_words)
def bold_it(item):
  return '\\textbf{' + item + '}'
italian_words = list(map(bold_it, knwon_words))

val = list()
for ii in range(max_len):
  res = list()
  for jj in range(len(italian_words)):
    # print(english_words[jj][ii])
    res.append(english_words[jj][ii])
  val.append(res)

# ------------------------------------------------------------- #
# Process, produce output, result data
# ------------------------------------------------------------- #

step = 4
tables = list()
for ii in range(0, len(english_words), step):
  print('Procesing sublock no.{}'.format(ii))
  val = list()
  for jj in range(max_len):
    print(jj)
    res = list()
    for zz in range(step):
      print(zz)
      res.append(english_words[zz+ii][jj])
    val.append(res)
  tables.append(val)

tables_str = list()
for table in tables:
  print('Processing...')
  table_str = list()
  lens = list()
  for ii in range(step):
    print(table[0:-1][ii])
    res = max(map(len, table[0:-1][ii]))
    lens.append(res)
  l = list()
  for xx in lens:
    l.append('%{}s'.format(xx))
  res_x = ' & '.join([xi for xi in l])
  print(res_x)
  for row in table:
    # res = ' & '.join([xi for xi in row])
    print(tuple(row))
    res = copy.deepcopy(res_x) % tuple(row)
    table_str.append(res + ' \\\\\n')
  tables_str.append(table_str)
  pprint(table_str)

# ------------------------------------------------------------- #
# Write results as output data
# ------------------------------------------------------------- #
for ii, table in enumerate(tables_str):
  with open('out.txt'.format(str(ii)), "a") as f:
    print('write table on file...')
    f.write('\n')
    f.write('\n')
    iw = italian_words[ii*step:(ii+1)*step]
    res = ' & '.join([xi for xi in iw]) 
    f.write(res + ' \\\\\n')
    f.write('\\hline\n')
    f.writelines(table)



def main() -> None:
  # ------------------------------------------------------------- #
  # Read input data
  # ------------------------------------------------------------- #

  with open('input.txt') as f:
    val = f.read()
  pass


if __name__ == '__main__':
  pass