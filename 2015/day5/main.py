def checkVowel(s):
  limit = 0
  for char in s:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
      limit += 1
  return limit >= 3

def appearTwice(s):
  for i in range(1,len(s)):
    if s[i-1] == s[i]:
      return True

def specialSubString(s):
  if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
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




nice = 0
filepath = 'test_part2.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    if checkVowel(line) and appearTwice(line) and specialSubString(line):
      nice += 1
    line = fp.readline()

print(nice)