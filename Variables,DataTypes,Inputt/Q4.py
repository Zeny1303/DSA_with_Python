# Swap two Numbers (without 3rd variable )
a= int(input("enter a no"))
b= int(input("enter a no"))
print(f"the value before swap of  a is {a} and b is {b}")
a=a+b   # 6+4=10
b=a-b    # 10 - 4=6
a= a-b # 10-6=4
print(f"the value after swap of  a is {a} and b is {b}")