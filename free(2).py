def xor(a, b):
     if not (a and b):
          if a or b:
               return 1
          return 0
     else:
          return 0
def bitor(a, b):
     a=str(a)
     b=str(b)
     ret=""
     for i in range(len(a)):
          ret+= str(int(a[i]) or int(b[i]))
     return ret


def bitand(a, b):
     a=str(a)
     b=str(b)
     ret=""
     for i in range(len(a)):
          ret+= str(int(a[i]) and int(b[i]))
     return ret


def bitxor(a, b):
     a=str(a)
     b=str(b)
     ret=""
     for i in range(len(a)):
          ret+= str(xor(int(a[i]), int(b[i])))
     return ret
print(bitxor(1011, 1000))
print(bitor(1011, 1000))
print(bitand(1011, 1000))
