import bintodec
def findTwoscomplement(str): #function for two's complement used for converison of dec to signed binary
    n = len(str) 
    i = n - 1
    while(i >= 0): 
        if (str[i] == '1'): 
            break
  
        i -= 1
    if (i == -1): 
        return '1'+str
    k = i - 1
    while(k >= 0): 
        if (str[k] == '1'): 
            str = list(str) 
            str[k] = '0'
            str = ''.join(str) 
        else: 
            str = list(str) 
            str[k] = '1'
            str = ''.join(str) 
  
        k -= 1
    return str
  
def dectobin(dec):            #function to convert dec to unsigned binary
  return bin(dec).replace("0b","")

def dectosignedbin(dec):           #function to convert dec ro signed binary
  if dec>=0:
    bin_str = bin(dec).replace("0b","")
    while(len(bin_str)!=40):
      bin_str = "0"+bin_str
    
    return bin_str

  else:
    dec *= -1
    bin_str = bin(dec).replace("0b","")

    while(len(bin_str)!=40):
      bin_str = "0"+bin_str

    return findTwoscomplement(bin_str)

    