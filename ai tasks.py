def string_same(str1, str2):
     if len(str1) != len(str2):
          print("Invalid input")
          return
     cnt= 0
     for i in range(len(str1)):
          if str1[i] == str2[i]:
               print(str1[i])
               cnt+=1
     print(cnt)


