# Question 13. Write a program to assign grades based on marks (if-else ladder)
marks = int(input("Enter your marks !!"))

if marks < 40:
    print("fail")
elif  marks <=50:
    print("C grade")  
elif marks <=65:
    print("B grade")
elif marks <=80:
    print("A grade")  
elif marks <=90:
    print("A+ grade")      
elif marks <=100:
    print("A++ garde")
else:
    print("not valid ")    
