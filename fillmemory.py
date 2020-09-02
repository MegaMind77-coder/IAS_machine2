                                           #fills 1000 * 40 bit memory based on user input from text file 
file1 = open("./input3.txt",'r')          #opens input file to input instructions
lines = file1.readlines()                #lines array containing instructions and data  given by user
memory = []
pc = 0
flag = 0
x=1
null_memory_ele = '0000000000000000000000000000000000000000'     #40 bit to fill up empty space in memory

for i in range(len(lines)):
  lines[i] = lines[i].strip('\n')
  idx = lines[i][0:4]
  idx = int(idx)
  while(x!=idx):
    memory.append(null_memory_ele)
    x+=1
  memory.append(lines[i][5:])
  x += 1
  if(flag == 0):
    pc = idx
    flag = 1

while idx!=1000:
  memory.append('0000000000000000000000000000000000000000')       
  idx+=1

file2 = open('memory.txt', 'w')            #memory.txt will store content of memory before execution of instructions begin

for x in memory:
  file2.write(x+'\n')

  
