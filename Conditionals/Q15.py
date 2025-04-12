# Question 15. Take 3 sides of a triangle and check if it's valid or not.

a = int(input("enter first side  ^_^"))
b = int(input("enter first side  :)"))
c = int(input("enter first side  ;)"))

if a>0 and b>0 and c>0:
    print("A VALID TRIANGLE")
    if a+b>c  and a+c>b and b+c> a:
        if a == b == c:
            print("Equailateral triangle ")
        elif a==b or b==c or c==a :
            print("Isosceles triangle  ")  
        else:
            print("saclane triangle") 
         
else:
    print("NOT VALID")

