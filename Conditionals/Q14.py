# Question 14. Check if a year is a leap year. 

year = int(input("Enter a year!!"))

if year%4==0 and (year%100 != 0 or year%400 == 0 ):
    print("leap year")
else:
    print("not a leap year")    
    
    
    
   
    
