def valid_list(list):
     if list == []:
          return "Invalid input"
     for i in list:
          if type(i)!= int:
               return "Invalid input"


def unique_nums(list):
     l = []
     for i in list:
          if i not in l:
               l.append(i)
     j=0
     for i in l:
          j+=1
     print(j)
               
def smallest_num(list):
     list = list.sort()
     print(list[0])

def largest_num(list):
     list = list.sort()
     print(list[-1])

def avg_list(list):
     sum_=0
     count =0
     for i in list:
          count= count+1
          sum_+= i
     print(sum_/count)



avg_list([1, 2, 3, 4])
