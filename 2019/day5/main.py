filepath = 'input.txt'
with open(filepath) as fp:
  line = fp.readline()
  while line:
    line = [int(x) for x in line.split(",")]
    line[1] = 12
    line[2] = 2
    start = 0
    for i in range(0,len(line),4):
      code = line[start:start + 4]
      start += 4
      opcode,pos1,pos2,store = code[0],code[1],code[2],code[3]
      if opcode == 1:
        line[store] = line[pos1] + line[pos2]
      elif opcode == 2:
        line[store] = line[pos1] * line[pos2]
      elif opcode == 99:
        print(line[0])
        print("End of Program")
        break
      else:
        print("Error")
        break
    line = fp.readline()