class Stack:
     def __init__(self):
          self.data = []

     def peek(self):
          return self.data[-1]

     def push(self, item):
          self.data.append(item)

     def pop(self):
          if self.isEmpty():
               print("[ ERROR ]: STACK UNDERFLOW")
               return None
          return self.data.pop()

     def isEmpty(self):
          if self.data == []:
               return True
          return False

     def display(self):
          if self.isEmpty():
               print("[]")
               return
          print("[ ", end="")
          for i in self.data:
               print(i, end=" ")
          print("] <- Top")

     def fdisplay(self):
          if self.isEmpty():
               print("|  |")
               print("+--+")
               return
          for i in self.data[::-1]:
               print("|{:^4}|".format(i))
          print("+----+")


def precedenceCheck(op1, op2):
     if op1 == op2:
          return "="
     precedence = {"^": 3, "*": 2, "/": 2, "-": 1, "+": 1}
     if (precedence[op1] - precedence[op2]) > 0:
          return ">"
     else:
          return "<"


def operationCheck(i, stk, result):
     if stk.isEmpty() or stk.peek() == "(":
          stk.push(i)
          return stk, result
     elif i == ")":
          while (not stk.isEmpty()) and (stk.peek() != "("):
               result += stk.pop()
          if not stk.isEmpty():
               stk.pop()
          return stk, result
     elif precedenceCheck(i, stk.peek()) == ">":
          stk.push(i)
          return stk, result
     elif precedenceCheck(i, stk.peek()) == "<":
          result += stk.pop()
          return operationCheck(i, stk, result)
     elif precedenceCheck(i, stk.peek()) == "=":
          if i == "^":
               result += stk.pop()
          stk.push(i)
          return stk, result


def infixToPostfix(infix):
     stk = Stack()
     infix = infix.split()
     result = ""
     for i in infix:
          if i.isdigit():
               result += i
          else:
               stk, result = operationCheck(i, stk, result)
     while not stk.isEmpty():
          result += stk.pop()
     return result


def infixToPrefix(infix):
     infix = infix[::-1]
     infix = infix.replace("(", "@").replace(")", "#").replace("@", ")").replace("#", "(")
     result = infixToPostfix(infix)
     return result[::-1]


print(infixToPrefix(input("Enter the Infix Expression: ")))
