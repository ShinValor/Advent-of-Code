import re

def checkVowel(s):
  count = 0
  for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
      count += 1
  return count >= 3

def appearTwice(s):
  return re.search(r'(.)\1',s)

def specialSubString(s):
  for i in ["ab", "cd", "pq", "xy"]:
    if i in s:
      return False
  return True

nice = 0
filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    if checkVowel(line) and appearTwice(line) and specialSubString(line):
      nice += 1
    line = fp.readline()

print(nice)


# Part Two

def twoPairs(s):
  return re.search(r'(.)(.).*\1\2',s)

def palindrome(s):
  return re.search(r'(.).\1',s)

nice = 0
filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    if twoPairs(line) and palindrome(line):
      nice += 1
    line = fp.readline()

print(nice)