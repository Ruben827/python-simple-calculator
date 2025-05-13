# simple calculator application
print("Calculator Application")

first_number = float(input("Input the first number: "))
operator = input("Input the operator (+, -, *, /): ")
second_number = float(input("Input the second number: "))

if operator == "+":
    print("The result is: ", first_number + second_number)
elif operator == "-":
    print("The result is: ", first_number - second_number)
elif operator == "*":
    print("The result is: ", first_number * second_number)
else:
    print("The result is: ", first_number / second_number)





