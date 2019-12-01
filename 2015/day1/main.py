filepath = 'input.txt'
position = 0
d = {"(":0,")":0}
with open(filepath) as fp:
  line = fp.readline()
  for char in line:
    position += 1
    d[char] += 1

print(d["("]-d[")"])

# Part Two
filepath = 'input.txt'
position = 0
d = {"(":0,")":0}
with open(filepath) as fp:
  line = fp.readline()
  for char in line:
    position += 1
    d[char] += 1
    if d["("] - d[")"] < 0:
      print(position)
      break;