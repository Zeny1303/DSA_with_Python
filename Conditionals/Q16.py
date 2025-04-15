# Question 16. Check if a number is prime or not.

n = int(input("enter a number "))

for i in range(2,n-1):
    if n % i ==0 :
        print("not a prime no ")
        break
else: 
    print ("prime")   
        
