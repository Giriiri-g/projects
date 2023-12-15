def valid_list(l):
    if l==[]:
        return "Invalid input"
    for i in l:
        if type(i) != int:
            return "Invalid input"
    return "Valid input"

def unique_nums(l):
    x=[]
    cnt = 0
    for i in l:
        if i not in x:
            x.append(i)
            cnt+=1


def smallest_num(l):
    min_ = l[0]
    for i in l:
        if i<min_:
            min_ = i
    print(min_)

def largest_num(l):
    x=l[0]
    for i in l:
        if i>x:
            x = i
    print(x)

def avg_list(l):
    sum_ =0
    x= 0
    for i in l:
        sum_ +=i
        x+=1
    avg = sum_//x
    if avg<0:
        print(avg+1)
    else:
        print(avg)
        
    