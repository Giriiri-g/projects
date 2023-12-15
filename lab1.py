## [q1]

def disjunction(a, b):
     return (a or b)
def conjunction(a, b):
     return a and b
def exclusive_or(a, b):
     if not (a and b):
          if a or b:
               return 1
          return 0
     else:
          return 0
def negation(a):
     return bin(not a)[2]
print("\n\n\n")
print("+---+---+-----+")
print("| p | q | pVq |")
print("+---+---+-----+")
for i in range(2):
     for j in range(2):
          out = disjunction(i, j)
          print("| {} | {} |  {}  |".format(i, j, out))
          print("+---+---+-----+")
print("\n\n\n")
print("+---+---+-----+")
print("| p | q | p^q |")
print("+---+---+-----+")
for i in range(2):
     for j in range(2):
          out = conjunction(i, j)
          print("| {} | {} |  {}  |".format(i, j, out))
          print("+---+---+-----+")
print("\n\n\n")
print("+---+---+-----+")
print("| p | q | p⊕q |")
print("+---+---+-----+")
for i in range(2):
     for j in range(2):
          out = exclusive_or(i, j)
          print("| {} | {} |  {}  |".format(i, j, out))
          print("+---+---+-----+")
print("\n\n\n")
print("+---+----+")
print("| p | ¬p |")
print("+---+----+")
for i in range(2):
     out = negation(i)
     print("| {} | {}  |".format(i, out))
     print("+---+----+")

## [q2]


def _3wconjunction(a, b, c):
     return a and b and c
def _3wdisjunction(a, b, c):
     return a or b or c
def _3wexclusive_or(a, b, c):
     if not (a and b and c):
          if a or b or c:
               return 1
          return 0
     return 0
print("+---+---+---+-------+")
print("| p | q | r | pVqVr |")
print("+---+---+---+-------+")
for i in range(2):
     for j in range(2):
          for k in range(2):
               out = _3wdisjunction(i, j, k)
               print("| {} | {} | {} |   {}   |".format(i, j, k, out))
               print("+---+---+---+-------+")
print("\n\n\n")
print("+---+---+---+-------+")
print("| p | q | r | p^q^r |")
print("+---+---+---+-------+")
for i in range(2):
     for j in range(2):
          for k in range(2):
               out = _3wconjunction(i, j, k)
               print("| {} | {} | {} |   {}   |".format(i, j, k, out))
               print("+---+---+---+-------+")
print("\n\n\n")
print("+---+---+---+-------+")
print("| p | q | r | p⊕q⊕r |")
print("+---+---+---+-------+")
for i in range(2):
     for j in range(2):
          for k in range(2):
               out = _3wexclusive_or(i, j, k)
               print("| {} | {} | {} |   {}   |".format(i, j, k, out))
               print("+---+---+---+-------+")
## [q3]


def conditional(p, q):
     return bin((not p) or q)[2]
def biconditional(p, q):
     return bin(((not p) or q) and ((not q) or p))[2]

print("\n\n\n")
print("+---+---+-----+")
print("| p | q | p→q |")
print("+---+---+-----+")
for i in range(2):
     for j in range(2):
          out = conditional(i, j)
          print("| {} | {} |  {}  |".format(i, j, out))
          print("+---+---+-----+")


print("\n\n\n")
print("+---+---+-----+")
print("| p | q | p↔q |")
print("+---+---+-----+")
for i in range(2):
     for j in range(2):
          out = biconditional(i, j)
          print("| {} | {} |  {}  |".format(i, j, out))
          print("+---+---+-----+")


## [q4]


def f1(p, q):
     return bin((not p) or (p and q))[2]
def f2(p, q):
     return bin((not p) and (p and (not q)))[2]
def f3(p, q, r):
     return bin((p and q) or ((not q) and r))[2]

print("\n\n\n")
print("+---+---+-----+")
print("| p | q | pq  |")
print("+---+---+-----+")
for i in range(2):
     for j in range(2):
          out = f1(i, j)
          print("| {} | {} |  {}  |".format(i, j, out))
          print("+---+---+-----+")


print("\n\n\n")
print("+---+---+-----+")
print("| p | q | pq  |")
print("+---+---+-----+")
for i in range(2):
     for j in range(2):
          out = f2(i, j)
          print("| {} | {} |  {}  |".format(i, j, out))
          print("+---+---+-----+")


print("\n\n\n")
print("+---+---+---+-------+")
print("| p | q | r | pqr   |")
print("+---+---+---+-------+")
for i in range(2):
     for j in range(2):
          for k in range(2):
               out = f3(i, j, k)
               print("| {} | {} | {} |   {}   |".format(i, j, k, out))
               print("+---+---+---+-------+")

## [q5]

def xor(a, b):
     if not (a and b):
          if a or b:
               return 1
          return 0
     else:
          return 0


def chk_bin(a):
     a = a.replace("0", "")
     a = a.replace("1", "")
     if a != "":
          return False
     return True


def prep(a, b):
     a = str(a)
     b = str(b)
     if not (chk_bin(a) and chk_bin(b)):
          print("[Invalid input] : bitor() takes only bin number as input.")
          return None, None
     if len(a)>len(b):
          b = (len(a)-len(b))*"0" + b
     else:
          a = (len(b)-len(a))*"0" + a
     return a, b


def bitor(a, b):
     a, b = prep(a, b)
     if a == None:
          return
     ret = ""
     for i in range(len(a)):
          ret+= str(int(a[i]) or int(b[i]))
     return ret


def bitand(a, b):
     a, b = prep(a, b)
     ret = ""
     if a == None:
          return
     for i in range(len(a)):
          ret+= str(int(a[i]) and int(b[i]))
     return ret


def bitxor(a, b):
     a, b = prep(a, b)
     ret = ""
     if a == None:
          return
     for i in range(len(a)):
          ret+= str(xor(int(a[i]), int(b[i])))
     return ret
print(bitxor(1011, 1000))

## [q6]
def f4(p, q, r):
     return int((p and (not q)) and (p and (not q)))

print("\n\n\n")
print("+---+---+---+-------+")
print("| p | q | r | out   |")
print("+---+---+---+-------+")
for i in range(2):
     for j in range(2):
          for k in range(2):
               out = f4(i, j, k)
               print("| {} | {} | {} |   {}   |".format(i, j, k, out))
               print("+---+---+---+-------+")


def f5(p, q, r):
     return int(p and ((not q) or (not r)))

print("\n\n\n")
print("+---+---+---+-------+")
print("| p | q | r | out   |")
print("+---+---+---+-------+")
for i in range(2):
     for j in range(2):
          for k in range(2):
               out = f5(i, j, k)
               print("| {} | {} | {} |   {}   |".format(i, j, k, out))
               print("+---+---+---+-------+")

chkkk = True
for i in range(2):
     for j in range(2):
          for k in range(2):
               if f5(i, j, k)!=f4(i, j, k):
                    print("Not Equivalent!")
                    chkkk = False
                    break
if chkkk:
     print("Equivalent!")
          
