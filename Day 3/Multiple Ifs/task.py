# roller cosaster bill maker
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <12:
        # print("You need to pay 5$")
        bill += 5
    elif age <= 18:
        # print("You need to pay 7$")
        bill += 7
    else:
        # print("You need to pay  12$")
        bill += 12

    wants_photo= input("Do you need a photo? (Y/N):")
    if wants_photo == "y":
        bill += 3
        print(f"your Bill is : {bill}")
    if wants_photo == "n":
        print(f"Your Bill is  : {bill}")


else:
    print("Sorry you have to grow taller before you can ride.")
