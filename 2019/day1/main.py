import math

res = 0

filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    num = int(line)
    fuel = math.floor(num/3)-2
    res += fuel
    line = fp.readline()

print(res)

# Part Two
import math

res = 0

filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    num = int(line)
    fuel = math.floor(num/3)-2
    res += fuel
    fuel = math.floor(fuel/3)-2
    while fuel > 0:
      res += fuel
      fuel = math.floor(fuel/3)-2
    line = fp.readline()

print(res)