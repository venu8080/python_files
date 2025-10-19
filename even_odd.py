even=0
odd=0
n=int(input("Enter how many numbers you want to input: "))
for i in range(n):
    num = int(input(f"Enter number {i+1}:"))
    if num%2== 0:
        even=+1
    else:
        odd=+1
print("Total even numbers:",even)
print("Total odd numbers:",odd)
