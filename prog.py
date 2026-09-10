# calculator 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter sec number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":

    if num2 != 0:
        print("Result:", num1 / num2)

    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")


#factorial

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact*i

print("Factorial:", fact)


# fibonacci series

n = int(input("Enter number of terms: "))
a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

#even or odd check

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# prime number check

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a Prime Number")

else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")

    else:
        print("Not a Prime Number")


# palindrome number

num = input("Enter a num: ")

if num == num[::-1]:
    print("Palindrome Number")

else:
    print("Not a Palindrome Number")


# Armstrong Number

num = int(input("Enter a num : "))
digits = str(num)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)

if total == num:
    print("Armstrong Number")

else:
    print("Not an Armstrong Number")


# Reverse a Number

num = input("Enter a number: ")

print("Reverse:", num[::-1])


#conditional statement

light = input("light:")

if(light == "red"):
     print("stop")

elif(light == "yellow:"):
     print("look")

elif(light == "green:"):
     print("go")

else:
     print("broken light")


 # find greatest of three numbers

a = int (input(" enter the value of a:"))
b = int (input(" enter the value of b:"))
c = int (input(" enter the value of :c"))

if((a>b)and(a>c)):
    print("a is greater")

elif((b>a)and(b>c)):
    print(" b is greater")

else:
    print("c is greater")



# check the num is multiple of 5 or not

    num = int (input("enter the num:"))

if(num%5==0):
    print("multiple of 5")

else:
    print("not a multiple of 5")


# table of any number 
n = int(input('enter the vlaue of n:'))
i = 1

while i<=10:

    print(n*i)
    i=i+1


# count vowels in a string 

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in string:

    if char in vowels:
        count += 1

print("Number of vowels:", count)


# simple calculator

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", a + b)

elif operator == "-":
    print("Result:", a - b)

elif operator == "*":
    print("Result:", a * b)

elif operator == "/":

    if b != 0:
        print("Result:", a / b)

    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")