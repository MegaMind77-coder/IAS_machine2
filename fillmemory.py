file1 = open("./input1.txt",'r')
lines = file1.readlines()
memory = []
pc = 0
flag = 0
x=1
null_memory_ele = '0000000000000000000000000000000000000000'

for i in range(len(lines)):
  lines[i] = lines[i].strip('\n')
  idx = lines[i][0:3]
  idx = int(idx)
  while(x!=idx):
    memory.append(null_memory_ele)
    x+=1
  memory.append(lines[i][4:])
  x += 1
  if(flag == 0):
    pc = idx
    flag = 1

while idx!=1000:
  memory.append('0000000000000000000000000000000000000000')
  idx+=1

file2 = open('memory.txt', 'a')

for x in memory:
  file2.write(x+'\n')

  
