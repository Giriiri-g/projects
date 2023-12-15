#WAP to find if a string is a palindrome

#                                                       PALINDROME
#                                                       __________


pal = False
while pal == False:
    x = input("\nplease enter a palindrome :")
    rev = x[::-1]
    if x == rev:
        pal = True
        print("\nThe given string is a palindrome :", x)
    else:
        print("\ngiven string is not a palindrome, please enter a palindrome")
