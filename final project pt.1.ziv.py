import time
print("hello, this is my final project")
name = input("what is your name? ")
print("hi " + name + ", nice to meet you")
print("this is a special calculator, i would need two numbers from you")
num1 = int(input("first number "))
num2 = int(input("second number "))
print("thank you for putting in your number " + str(num1) + " and " +str(num2))
even_odd_str = ""
if num1 % 2 == 0:
    even_odd_str = "even"
else:
    even_odd_str = "odd"
print("i can see that the first number is " + even_odd_str)
even_odd_str2 = ""
if num2 % 2 == 0:
    even_odd_str2 = "even"
else:
    even_odd_str2 = "odd"
print("and the second is " + even_odd_str2)
if num1 % 2 == 0 and num2 % 2 == 0:
    print("so both even")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("so both are odd")
else:
    print("so one is even and the second is odd")
total = ""
operator = input("operator (+, -, *, /) ")
if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("error: cannot be divided by " + str(num2))
        print("an error had accrued, please try again")
    else:
        answer = input("you chose division, should the result be integer? (y/n) ") 
        if answer == "y":
            total = num1 // num2
        else:
            total = num1 / num2
if total != "":
    print(str(num1) + operator + str(num2) + "=" + str(total))
else:
    print("error: " + operator + " is not supported")
    print("an error had accured, please try again")
print("thank you " + name + " for using the calcutalor on " + time.ctime())
