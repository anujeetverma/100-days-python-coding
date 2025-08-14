try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed in a invalid number please try an numerical response eg 15")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
