import re

def adjacent(num):
  num = str(num)
  for i in range(1,len(num)):
    if num[i] == num[i-1]:
      return True
  return False

def increasing(num):
  num = str(num)
  for i in range(1,len(num)):
    if num[i] < num[i-1]:
      return False
  return True 

counter = 0
for i in range(153517,630395+1):
  if adjacent(i) and increasing(i):
    counter += 1

print(counter)

# Part Two
def adjacent2(num):
  num = str(num)
  for i in range(1,len(num)):
    if num[i] == num[i-1] and num.count(num[i]) == 2:
      return True
  return False

# print(adjacent2(112233))
# print(adjacent2(123444))
# print(adjacent2(111122))

counter = 0
for i in range(153517,630395+1):
  if adjacent2(i) and increasing(i):
    counter += 1

print(counter)