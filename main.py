val="""sorgere\n
arise, rise, spring, crop up, spring out\n
insorgere\n
arise, rise, rise up, riot\n
derivare\n
derive, result, arise, come, stem, follow\n
presentarsi\n
appear, arise, report, turn up, spring up\n
nascere\n
be born, arise, rise, come, grow, originate\n
risultare\n
result, prove, arise, emerge, follow, come out\n
alzarsi\n
rise, arise, heave, spring up, stir, shoot up\n
levarsi\n
rise, arise, get up, take off, stand up\n
sopravvenire\n
occur, arise\n
sollevare\n
lift, raise, relieve, rise, hoist, arise\n
svegliarsi\n
wake, awake, rouse, arise\n
offrirsi\n
offer, offer oneself, arise\n
"""
# ------------------------------------------------------------- #

# print(val)
res = val.split('\n')
# print(res)
res = filter(lambda xi: len(xi) > 0, res)
res = list(res)

italian_words = list(map(str.capitalize, res[0:-1:2]))
english_words = res[1::2]

print(len(italian_words), len(english_words))
assert len(italian_words) == len(english_words), 'different lenghts'

english_words = map(lambda xi: xi.strip().split(','), english_words)
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
  for jj in range(len(italian_words)):
    # print(english_words[jj][ii])
    res.append(english_words[jj][ii])
  res = ' & '.join([xi for xi in res])
  val.append(' & ' + res + ' \\\\\n')

pprint(val)
with open('out.txt', "w") as f:
  f.writelines(val)

# ------------------------------------------------------------- #
print(max_len)
print(italian_words)
def bold_it(item):
  return '\\textbf{' + item + '}'
italian_words = list(map(bold_it, italian_words))

val = list()
for ii in range(max_len):
  res = list()
  for jj in range(len(italian_words)):
    # print(english_words[jj][ii])
    res.append(english_words[jj][ii])
  val.append(res)
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


pprint(tables)

# import sys
# sys.exit(0)

tables_str = list()
for table in tables:
  print('Processing...')
  table_str = list()
  for row in table:
    res = ' & '.join([xi for xi in row])
    table_str.append(res + ' \\\\\n')
  tables_str.append(table_str)
  pprint(table_str)

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