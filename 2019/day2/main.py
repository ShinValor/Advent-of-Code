filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    line = [int(x) for x in line.split(",")]
    line[1] = 12
    line[2] = 2
    # print(line)
    start = 0
    for i in range(0,len(line),4):
      code = line[start:start + 4]
      start += 4
      opcode,pos1,pos2,store = code[0],code[1],code[2],code[3]
      if opcode == 1:
        # print(opcode,pos1,pos2,store)
        line[store] = line[pos1] + line[pos2]
      elif opcode == 2:
        # print(opcode,pos1,pos2,store)
        line[store] = line[pos1] * line[pos2]
      elif opcode == 99:
        print(line[0])
        print("End of Program")
        break
      else:
        print("Error")
        break
    line = fp.readline()

# Part Two
def gravity(noun,verb):
  filepath = 'input.txt'
  with open(filepath) as fp:
    line = fp.readline()
    while line:
      line = [int(x) for x in line.split(",")]
      line[1] = noun
      line[2] = verb
      # print(line)
      start = 0
      for i in range(0,len(line),4):
        code = line[start:start + 4]
        start += 4
        opcode,pos1,pos2,store = code[0],code[1],code[2],code[3]
        if opcode == 1:
          # print(opcode,pos1,pos2,store)
          line[store] = line[pos1] + line[pos2]
        elif opcode == 2:
          # print(opcode,pos1,pos2,store)
          line[store] = line[pos1] * line[pos2]
        elif opcode == 99:
          return line[0]
          break
        else:
          print("Error")
          break
      line = fp.readline()

for i in range(99):
  for j in range(99):
    if gravity(i,j) == 19690720:
      print(i,j)
      print((100*i)+j)