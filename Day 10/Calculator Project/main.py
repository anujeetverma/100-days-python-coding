import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
n1 = int(input("What's the first number: "))
cont = "y"
while cont == "y":

    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Pick an operation: ")
    n2 = int(input("What's the next number: "))
    if operation == "+":
        n1 = add(n1 , n2)
    elif operation == "-":
        n1 = sub(n1 , n2)
    elif operation == "*":
        n1 = mul(n1 , n2)
    elif operation == "/":
        n1 = div(n1 , n2)
    cont = input(f"Type 'y' to continue with {n1} or type 'n' to stop the calculation")
print(f"The final answer = {n1}")
