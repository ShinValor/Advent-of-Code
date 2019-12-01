x,y = 0,0 # X,Y coordinates
houses = [[x,y]]
filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    for direction in line:
      # print(x,y,direction)
      if direction == "^":
        # print("up")
        y += 1
      elif direction == ">":
        # print("right")
        x += 1
      elif direction == "v":
        # print("down")
        y -= 1
      else:
        # print("left")
        x -= 1
      if [x,y] not in houses:
        houses.append([x,y])
    line = fp.readline()

print(len(houses))

# Part Two
x1,y1 = 0,0 # X,Y coordinates
x2,y2 = 0,0
turn = True # True is Santa, False is Robot
houses = [[0,0]]
filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    for direction in line:
      if turn == True:
        if direction == "^":
          y1 += 1
        elif direction == ">":
          x1 += 1
        elif direction == "v":
          y1 -= 1
        else:
          x1 -= 1
        if [x1,y1] not in houses:
          houses.append([x1,y1])
      else:
        if direction == "^":
          y2 += 1
        elif direction == ">":
          x2 += 1
        elif direction == "v":
          y2 -= 1
        else:
          x2 -= 1
        if [x2,y2] not in houses:
          houses.append([x2,y2])
      turn = not turn
    line = fp.readline()

print(len(houses))