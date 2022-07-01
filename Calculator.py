num1 = int(input("Introduceti un numar-> "))
num2 = int(input("Enter another number-> "))
operation = input("What math operation do you want to do? ")
result = 0
if "+" in operation:
    result = num1 + num2
elif "-" in operation:
    result = num1 - num2
elif "*" in operation:
    result = num1 * num2
elif "/" in operation:
    result = num1 / num2
elif "**" in operation:
    result = num1 ** num2
else:
    result = -1
    print("The operation is not available.")
print(f"The result is: {result}")
