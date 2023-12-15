def reverse_words_order_and_swap_cases(sentence):
     if type(sentence)!= str:
          return "[ERROR] : Invalid literal"
     elif "  " in sentence:
          return "[ERROR] : Invalid Format"
     elif sentence.count(" ")>9:
          return "[ERROR] : More than 10 words"
     elif not (sentence[0].isalpha() and sentence[-1].isalpha()):
          return "[ERROR] : The sentence has to start and end with a letter"
     s = ""
     for i in sentence:
          if i.isupper():
               s+=i.lower()
          elif i.islower():
               s+=i.upper()
          else:
               s+=" "
     sentence = s.split(" ")
     for u in sentence:
          if len(u)>10:
               return "[ERROR] : The word has exceeded the limit of 10-->", u 
     s = ""
     for i in range(len(sentence)):
          s+=sentence[-1-i]
          s+=" "
     return s
