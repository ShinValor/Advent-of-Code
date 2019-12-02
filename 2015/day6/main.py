lightGrid = [[0 for j in range(1000)] for i in range(1000)]

def toggle(x1,y1,x2,y2):
  return
 
def turn(x1,y1,x2,y2,switch):
  return

filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    line = line.split(" ")
    print(line)
    instruction = line[0]
    x1,x2,y1,y2 = None,None,None,None
    switch = None
    if instruction == "toggle":
      coordinates = line[1].split(",") + line[-1].split(",")
      x1,y1,x2,y2 = coordinates[0],coordinates[1],coordinates[2],coordinates[3]
    elif instruction == "turn":
      switch = line[1]
      coordinates = line[2].split(",") + line[-1].split(",")
      x1,y1,x2,y2 = coordinates[0],coordinates[1],coordinates[2],coordinates[3]
    else:
      print("Error")
      break
    print(x1,y1,x2,y2)
    if switch == "on":
      pass
    elif switch == "off":
      pass
    else:
      pass
    line = fp.readline()

print(sum([sum(x) for x in lightGrid]))