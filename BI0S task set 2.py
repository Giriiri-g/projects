## [ TRIANGLE CHOPSTICKS ]
"""
grey says less no of triagles can be formed than r; if True; she wins
natsu wants more triangles than r to win
inputs : a b r n
outputs:
$ total no of triangles
$ winner
"""
n = int(input("Enter the no. of test cases :"))
for k in range(n):
     abr = input("Enter the values of a,b,r:")
     a,b,r = tuple(abr.split(" "))
     tot = input("length of all sticks in the jar:")
     tot = tot.split(" ")
     tri = 0
     for i in tot:
          if (int(i)<int(a)+int(b)) and (int(i)!=0):
               tri += 1
     print(tri)
     if r<tri:
          print("Natsu")
     else:
          print("Grey")

## [ SECRET IMAGES ]

"""
replace space with dot
split the string withh dot as parameter
count using each variable in a dict
d ={'png':0, 'bmp':0, 'jpeg':0}
if i in d:
     d[i] +=1
"""
s = input("Enter your Data: ")
s = s.replace(" ", ".")
s= s.split(".")
d = {'png':0, 'bmp':0, 'jpeg':0}
for i in s:
     if i in d:
          d[i]+=1
print(d[0], d[1], d[2])



## [READING EMAILS]

"""
id, domain, extension
for valid id: !#$%^&*{}|~_+-=/'        '.' connot be in first or t position of id    0-9
for valid domain : - is allowed in first or last position,   0-9 allowed, but not entirely numeric
for valid extension : width is 3, no special characters
"""
def verify(email):
email = input("Enter teh email ID: ")
if not ('@' in email and email[-4] == '.'):
     print(False)
elif not email[-4:].isaplha():
     print(False)
