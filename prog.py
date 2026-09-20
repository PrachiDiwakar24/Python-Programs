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


# check whether a num is positive , negative ,or zero

num = int(input("Enter a num: "))

if num > 0:
    print("Positive number")

elif num < 0:
    print("Negative number")

else:
    print("Zero")


# leap year or not

year = int(input("Enter a year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
    
else:
    print("Not a leap year")


 # average of three numbers 

def print_avg(a,b,c):
    avg = (a+b+c)/2
    print(avg)
    return avg

print_avg(5,1,2)


#waf to print the length of the list 

cities = ['mumbai','pune','delhi','noida','chennai','gurgaon']
fruits = ['mango','apple','grapes','peach']

def print_len(list):
    print(len(list)) 
print_len(cities)
print_len(fruits)


# factorial of n num

def fact(n):
    if(n==0 or n==1 ):
      return 1
    return fact(n-1)*n
print(fact(7))



# Student Grade Calculator

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n ----Student Result---- ")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)



# Electricity Bill Calculator

units = float(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
    
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print("Electricity Bill =", bill)


# dictonary 
dict = {
    "name":" prachi",
    "cgpa": 9.3,
    "subject":"python",
}
print(dict.keys())
print(len(dict.keys()))
print(dict)
print(type(dict))
print(dict["name"])
dict["name"]= "geeta"
print(dict)
null_dict = {}  #empty dict
print(null_dict)


# factorial using while loop
n = 5
fact = 1
i = 1
while i<=n:
    fact = fact*i
    i += 1
print(fact)


# Voting Eligibility Checker

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# waf for even or odd
n = int(input("enter the value of n:"))
def calc_num(n):
  if n%2==0:
    print("even")
  else:
    print("odd")
calc_num(n)


# reverse counting

def show(n):
    if n==0:  # base case
        return
    print(n)
    show(n-1)
show(5)

#waf to find factorial of n 
n = 7
def calc_fact(n):
     fact = 1
     for i in range(1,n+1):
        fact= fact*i
     print(fact)
calc_fact(7)
    