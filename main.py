import bintodec
import fillmemory
import dectobin

class MAR():
    address = ''
    pointer_value = 0
    def __init__(self):
        self.address = '000000000000'
        self.pointer_value = 12

def showchanges(ac, mbr, ibr, ir, mar, pc):
    if(ac == ''):
        print("AC = ",ac)
    else:
        print("AC = ",ac, "Decimal value of AC = ", bintodec.signedbintodec(bintodec.bintodec(ac), 40))
    print("MBR = ", mbr)
    print("IBR = ", ibr)
    if(ir == ''):
        print("IR = ", ir)
    else:
        print("IR = ", ir, "Decimal value of IR = ", bintodec.bintodec(ir))
    
    if(mar == ''):
        print("MAR = ", mar)
    else:
        print("MAR = ", mar, "Decimal value of MAR = ", bintodec.bintodec(mar))
    print("PC = ", pc+1)
    print()


if __name__ == "__main__":
    
    memory = fillmemory.memory
    pc = fillmemory.pc - 1
    ir = ''        #8 bit IR
    ibr = ''       #20 bit IBR
    mar = ''       #12 bit MAR
    mbr = ''       #40 bit MBR
    ac = ''        #40 bit AC
    mq = ''        #40 bit MQ

    execution = True

    while(execution):
        if (ibr == ''):
            mar = dectobin.dectobin(pc)
            mbr = memory[bintodec.bintodec(mar)]

            if(bintodec.bintodec(mbr[0:20]) == 0):
                ir = mbr[20:28]
                mar = mbr[28:40]
                pc = pc + 1
            else:
                ibr = mbr[20:40]
                ir = mbr[0:8]
                mar = mbr[8:20]
        else:
            ir = ibr[0:8]
            mar = ibr[8:20]
            pc = pc + 1
            ibr = ''
        showchanges(ac, mbr, ibr, ir, mar, pc)
        
        if(bintodec.bintodec(ir) == 1):            #LOAD M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            ac = mbr

        elif(bintodec.bintodec(ir) == 5):          #ADD M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            mbr_dec = bintodec.signedbintodec(bintodec.bintodec(mbr), 40)
            ac = dectobin.dectosignedbin(bintodec.signedbintodec(bintodec.bintodec(ac), 40) + mbr_dec)

        elif(bintodec.bintodec(ir) == 33):    #STOR M(X) INSTRUCTION
            memory[bintodec.bintodec(mar) - 1] = ac
            change_location = bintodec.bintodec(mar)
            print('Memory at {} changed to {}'.format(change_location, memory[bintodec.bintodec(mar) - 1]))
            print()

        elif(bintodec.bintodec(ir) == 6):    #SUB M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            mbr_dec = bintodec.signedbintodec(bintodec.bintodec(mbr), 40)
            ac = dectobin.dectosignedbin(bintodec.signedbintodec(bintodec.bintodec(ac), 40) - mbr_dec)

        elif(bintodec.bintodec(ir) == 15):   #JUMP +M(X, 0:19) INSTRUCTION
            ac_dec = bintodec.signedbintodec(bintodec.bintodec(ac), 40)
            if(ac_dec > 0):
                pc = bintodec.bintodec(mar) - 1
                ibr = ''

        elif(bintodec.bintodec(ir) == 14):  #JUMP +M(X, 20:39) INSTRUCTION
            ac_dec = bintodec.signedbintodec(bintodec.bintodec(ac), 40)
            if(ac_dec > 0):
                pc = bintodec.bintodec(mar) - 1
                ibr = ''
                mbr = memory[bintodec.bintodec(mar) - 1]
                ibr = mbr[20:40]
                print(ibr)

        elif(bintodec.bintodec(ir) == 255):   #HALT INSTRUCTION
            execution = False
            file3 = open("out.txt", "w")
            for x in memory:
               file3.write(x+'\n')
            
            
        