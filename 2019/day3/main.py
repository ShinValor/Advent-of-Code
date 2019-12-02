filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    print(line)
    line = fp.readline()