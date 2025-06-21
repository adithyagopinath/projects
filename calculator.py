def addition(a,b):
    sum = a + b
    return sum

def subtraction(c,d):
    difference = c - d
    return difference 

def multiplication(e,f):
    product = e * f
    return product

def division(g,h):
    quotient = g / h
    return quotient

def calculator():
    print("Welcome to the simple calculator program!")
    cont = True
    
    while cont == True:
        operation = input("\nWhat operation would you like to conduct? Addition (a), Subtraction (s), Multiplication(m), or Division (d)? ").lower()
        while operation not in ['a', 'd', 's', 'm']:
            print("Incorrect input. Please input a valid operation (a, s, m, d). ")
            operation = input("\nAddition (a), Subtraction (s), Multiplication (m), or Division (d)? ").lower()
        num1 = float(input("Enter number 1. "))
        num2 = float(input("Enter number 2. "))
        if operation == "a":
            sum_op = addition(num1, num2)
            print(f"{num1} + {num2} = {sum_op}!")
        elif operation == "s":
            dif_op = subtraction(num1, num2)
            print(f"{num1} - {num2} = {dif_op}!")
        elif operation == "m":
            product_op = multiplication(num1, num2)
            print(f"{num1} * {num2} = {product_op}!")
        elif operation =="d":
            while num2 == 0:
                num2 = float(input("A number cannot be divided by 0. Please input a different number for number 2. "))
            quotient_op = division(num1, num2)
            print(f"{num1} / {num2} = {quotient_op}!")
        finished = input("Are you finished with your calculations? Enter y to quit. ").lower()
        if finished == 'y':
            cont = False
        
        
calculator()   
    
        
            

    
    