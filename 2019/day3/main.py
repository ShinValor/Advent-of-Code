x1,y1,x2,y2 = 0,0,0,0 # wire 1 and wire 2
filepath = 'input.txt'
path_1 = []
path_2 = []
wire_one_instructions = None
wire_two_instructions = None
with open(filepath) as fp:
  line = fp.readline()
  while line:
    line = line.split(",")
    if wire_one_instructions is None:
      wire_one_instructions = line
    else:
      wire_two_instructions = line    
    line = fp.readline()

for move in wire_one_instructions:
  direction = move[0]
  steps = int(move[1:])
  if direction == "U":
    for i in range(1,steps+1):
      path_1.append([x1,y1+i])
    y1 += steps
  elif direction == "R":
    for i in range(1,steps+1):
      path_1.append([x1+i,y1])
    x1 += steps
  elif direction == "D":
    for i in range(1,steps+1):
      path_1.append([x1,y1-i])
    y1 -= steps
  elif direction == "L":
    for i in range(1,steps+1):
      path_1.append([x1-i,y1])
    x1 -= steps
  else:
    print("Error")
    break


for move in wire_two_instructions:
  direction = move[0]
  steps = int(move[1:])
  if direction == "U":
    for i in range(1,steps+1):
      path_2.append([x2,y2+i])
    y2 += steps
  elif direction == "R":
    for i in range(1,steps+1):
      path_2.append([x2+i,y2])
    x2 += steps
  elif direction == "D":
    for i in range(1,steps+1):
      path_2.append([x2,y2-i])
    y2 -= steps
  elif direction == "L":
    for i in range(1,steps+1):
      path_2.append([x2-i,y2])
    x2 -= steps
  else:
    print("Error")
    break  

intersection = [list(x) for x in set(tuple(x) for x in path_1).intersection(set(tuple(x) for x in path_2))]

minimum_distance = float("inf")
for distance in intersection:
  minimum_distance = min(abs(distance[0]) + abs(distance[1]),minimum_distance)

print(minimum_distance)


# Part Two
minimum_steps = float("inf")
for distance in intersection:
  minimum_steps = min(path_1.index(distance)+path_2.index(distance)+2,minimum_steps)

print(minimum_steps)