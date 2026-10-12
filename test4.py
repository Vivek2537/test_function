#1.Write a function to which we pass a parameter and
#print the factors of a given number

def factor(n):
    for i in range(1,n+1):
        if n%i == 0:
            print(i)

num = int(input("enter the nuber"))
factor(num)


#2.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

3.

for i in range(22):
    print("*", end="")
print()

for i in range(10):
    print(" " * (20 - 2 * i)+ "*")

for i in range(21):
    print("*", end="")
print("*")