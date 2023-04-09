import re

inp = input('eNTER:' )

pat = r"^([1]?[0-9][0-9]?)?"

match = re.search(pat, inp)

if match:
  print('found', match.group(1))
else:
  print('did not find')


