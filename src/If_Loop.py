def addition(x, y):
    return x + y
  
def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


print("Select please one of the following operations: ")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

# In python, any inserted value is taken as True
while True:
    choice = input("What kind of operation should be performed? [Insert one of the options(1,2,3,4) or press Ctrl+c to quit]: ")

    if choice in ('1', '2', '3', '4'):
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x, "+", y, "=", addition(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtraction(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiplication(x, y))

        elif choice == '4':
            if y == 0:
                print ("Division by zero. We cannot perform this operation.")
            else:
                print(x, "/", y, "=", division(x, y))
       # break <<- If we want one-try-calculator
    else:
        print("There is no such an option. Select please one of the following: 1 2 3 4")
        
        
        
