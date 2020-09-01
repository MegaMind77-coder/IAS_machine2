import bintodec
import fillmemory
import dectobin

def mul(mbr, mq):
    mbr_dec = bintodec.signedbintodec(bintodec.bintodec(mbr), 40)
    mq_dec = bintodec.signedbintodec(bintodec.bintodec(mq), 40)
    result_dec = mbr_dec * mq_dec
    if(result_dec >=0):
        bin_str = bin(result_dec).replace("0b","")
        while(len(bin_str)!=80):
            bin_str = "0"+bin_str
        
        return bin_str

    else:
        result_dec *= -1
        bin_str = bin(result_dec).replace("0b","")

        while(len(bin_str)!=80):
            bin_str = "0"+bin_str
        return dectobin.findTwoscomplement(bin_str)

def div(mbr, ac):
    mbr_dec = bintodec.signedbintodec(bintodec.bintodec(mbr), 40)
    ac_dec = bintodec.signedbintodec(bintodec.bintodec(ac), 40)
    quo_dec = int(ac_dec/mbr_dec)
    rem_dec = ac_dec % mbr_dec 
    return_str = dectobin.dectosignedbin(rem_dec) + dectobin.dectosignedbin(quo_dec)
    return return_str

def decode(ir, mar):
    print("DECODE INSTRUCTION")
    if(bintodec.bintodec(ir) == 1):
        print("LOAD M({})".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 2):
        print("LOAD -M({})".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 5):
        print("ADD M({})".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 33):
        print("STOR M({})".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 6):
        print("SUB M({})".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 13):
        print("JUMP M({}, 0:19)".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 14):
        print("JUMP M({}, 20:39)".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 15):
        print("JUMP +M({}, 0:19)".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 16):
        print("JUMP +M({}, 20:39)".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 9):
        print("LOAD M({}), MQ".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 10):
        print("LOAD MQ")    
    elif(bintodec.bintodec(ir) == 11):
        print("MUL M({})".format(bintodec.bintodec(mar)))
    elif(bintodec.bintodec(ir) == 255):
        print("HALT")
    print()

def fetchchanges(ac, mq, mbr, ibr, ir, mar, pc):
    print("FETCHING INSTRUCTION")
    if(ac == ''):
        print("AC = ",ac)
    else:
        print("AC = ",ac, "Decimal value of AC = ", bintodec.signedbintodec(bintodec.bintodec(ac), 40))

    if(mq == ''):
        print("MQ = ")
    else:
        print("MQ = ",mq, "Decimal value of MQ = ", bintodec.signedbintodec(bintodec.bintodec(mq), 40))
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

def executechanges(ac, mq, mbr, ibr, ir, mar, pc):
    print("EXECUTE CHANGES")
    if(ac == ''):
        print("AC = ",ac)
    else:
        print("AC = ",ac, "Decimal value of AC = ", bintodec.signedbintodec(bintodec.bintodec(ac), 40))

    if(mq == ''):
        print("MQ = ")
    else:
        print("MQ = ",mq, "Decimal value of MQ = ", bintodec.signedbintodec(bintodec.bintodec(mq), 40))
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

def cycleEnd():
    print("End of cycle ----------------------------------------------------------")
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
        print("Current PC = ", pc + 1)
        print()
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

        fetchchanges(ac, mq, mbr, ibr, ir, mar, pc)

        decode(ir,mar)
        
        if(bintodec.bintodec(ir) == 1):            #LOAD M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            ac = mbr
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        elif(bintodec.bintodec(ir) == 2):         #LOAD -M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            ac = dectobin.dectosignedbin(-1*bintodec.signedbintodec(bintodec.bintodec(mbr), 40))
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)
        
        elif(bintodec.bintodec(ir) == 9):       #LOAD M(X), MQ INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            mq = dectobin.dectosignedbin(bintodec.signedbintodec(bintodec.bintodec(mbr), 40))
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        elif(bintodec.bintodec(ir) == 10):      #LOAD MQ INSTRUCTION
            ac = mq
            mq = ''
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        elif(bintodec.bintodec(ir) == 5):          #ADD M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            mbr_dec = bintodec.signedbintodec(bintodec.bintodec(mbr), 40)
            ac = dectobin.dectosignedbin(bintodec.signedbintodec(bintodec.bintodec(ac), 40) + mbr_dec)
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)


        elif(bintodec.bintodec(ir) == 33):    #STOR M(X) INSTRUCTION
            memory[bintodec.bintodec(mar) - 1] = ac
            change_location = bintodec.bintodec(mar)
            print('Memory at {} changed to {}'.format(change_location, memory[bintodec.bintodec(mar) - 1]))
            print()
            ac = ''
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        elif(bintodec.bintodec(ir) == 11):    #MUL M(X)
            mbr = memory[bintodec.bintodec(mar) - 1]
            result_bin = mul(mbr, mq)
            ac = result_bin[0:39]
            mq = result_bin[40:80]
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        elif(bintodec.bintodec(ir) == 6):    #SUB M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            mbr_dec = bintodec.signedbintodec(bintodec.bintodec(mbr), 40)
            ac = dectobin.dectosignedbin(bintodec.signedbintodec(bintodec.bintodec(ac), 40) - mbr_dec)
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        elif(bintodec.bintodec(ir) == 12):  #DIV M(X) INSTRUCTION
            mbr = memory[bintodec.bintodec(mar) - 1]
            result_bin = div(mbr, ac)
            ac = result_bin[0:40]
            mq = result_bin[40:80]
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)


        elif(bintodec.bintodec(ir) == 15):   #JUMP +M(X, 0:19) INSTRUCTION
            ac_dec = bintodec.signedbintodec(bintodec.bintodec(ac), 40)
            if(ac_dec > 0):
                pc = bintodec.bintodec(mar) - 1
                ibr = ''
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        elif(bintodec.bintodec(ir) == 16):  #JUMP +M(X, 20:39) INSTRUCTION
            ac_dec = bintodec.signedbintodec(bintodec.bintodec(ac), 40)
            if(ac_dec > 0):
                pc = bintodec.bintodec(mar) - 1
                ibr = ''
                mbr = memory[bintodec.bintodec(mar) - 1]
                ibr = mbr[20:40]
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

                
        elif(bintodec.bintodec(ir) == 13):  #JUMP M(X, 0:19) INSTRUCTION
            pc = bintodec.bintodec(mar) - 1
            ibr = ''
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)

        
        elif(bintodec.bintodec(ir) == 14):  #JUMP M(X, 20:39) INSTRUCTION
            pc = bintodec.bintodec(mar) - 1
            ibr = ''
            mbr = memory[bintodec.bintodec(mar) - 1]
            ibr = mbr[20:40]
            executechanges(ac, mq, mbr, ibr, ir, mar, pc)


        elif(bintodec.bintodec(ir) == 255):   #HALT INSTRUCTION
            execution = False
            file3 = open("out.txt", "w")
            for x in memory:
               file3.write(x+'\n')

        cycleEnd()
        
        
            
            
        