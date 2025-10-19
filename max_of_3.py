a = float(input("Enter first number:"))
b = float(input("Enter second number:"))
c = float(input("Enter third number:"))
if a>=b and a>= c:
    max=a
elif b>=a and b>=c:
    max=b
else:
    max=c
print("The maximum number is:", max)
