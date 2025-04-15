# Question 9 Check if a number is divisible by both 3 and 5 using logical operators.

a = int(input("enter a number"))
if a % 3 == 0 and a % 5 ==0 :
    print(f" {a} is  divisible by  both 3 and 5 ")
else:
    print(f" {a} is not divisible by  both 3 and 5 ")    
