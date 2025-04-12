# Question 20. Write a program to check if a given number is a palindrome. 

s = input("enter a string")
#slicing of string
reversed_string = s[ : :-1]
if s == reversed_string:
    print("tusi taan palindrome aa")
else:
    print("nah")    
