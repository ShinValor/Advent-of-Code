def surfaceArea(l,w,h):
  return 2*l*w + 2*w*h + 2*h*l

def smallestArea(l,w,h):
  return min(l*w,l*h,w*h)

def smallestPerimeter(l,w,h):
  return min(2*l+2*w,2*l+2*h,2*w+2*h)

def volume(l,w,h):
  return l*w*h

wrapping_paper = 0

filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    line = line.split("x")
    l,w,h = int(line[0]),int(line[1]),int(line[2])
    wrapping_paper += surfaceArea(l,w,h) + smallestArea(l,w,h)
    line = fp.readline()

print(wrapping_paper)

# Part Two
ribbon = 0

filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    line = line.split("x")
    l,w,h = int(line[0]),int(line[1]),int(line[2])
    ribbon += smallestPerimeter(l,w,h) + volume(l,w,h)
    line = fp.readline()

print(ribbon)
