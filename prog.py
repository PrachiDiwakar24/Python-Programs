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