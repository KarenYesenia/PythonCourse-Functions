# Write a function that receives as parameter one number 
# (must be a integer) and return the factorial of that number

def factorial(x):
    if x ==1:
        return 1
    else:
        return x * factorial(x-1)

x = int(input("Ingresa un número para la función factorial: "))
print(factorial(x))