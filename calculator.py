num = int(input("Enter the number: "))
symbol = ["+","-","*","/"]
op = input("Enter the operator: ")
num2 = int(input("enter the second nuber: "))
if op not in symbol:
    print("INVALID")

else:
    if op == "+":
        num = num2 + num
    elif op == "-":
        num = num - num2
    elif op == "*":
        num = num * num2
    else:
        if num2 == 0:
            print("Invald operation")
        else:
            num = num / num2
print(num)

