#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as start:
    print(start.read())

name_list = []
with open("./Input/Names/invited_names.txt") as file:
    for line in file:
        name = line.strip()
        if name:
            name_list.append(name)


for name in name_list:
    with open("./Input/Letters/starting_letter.txt", mode ="r") as file:
        letter = file.read()
        readyToSend = letter.replace("[name]", name)

        with open(f"./Output/ReadyToSend/{name}.txt",mode= "w") as final_letter:
            final_letter.write(readyToSend)


