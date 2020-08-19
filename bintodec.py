def bintodec(bin):
  return int(bin,2)


def signedbintodec(val, bits):
  if (val & (1 << (bits -1))) != 0 :
    val = val - (1 << bits)
  return val

