def bintodec(bin):              #function to convert unsigned binary to dec
  return int(bin,2)


def signedbintodec(val, bits):   #function to convert signed binary to dec
  if (val & (1 << (bits -1))) != 0 :
    val = val - (1 << bits)
  return val

