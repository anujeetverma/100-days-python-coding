def calculate_love_score(first_name, second_name):
    first_name_list = list(first_name)
    second_name_list = list(second_name)
    first_digit = 0
    second_digit = 0
    for letter in first_name_list:
        if letter == "t":
            first_digit += 1
        if letter == "r":
            first_digit += 1
        if letter == "u":
            first_digit += 1
        if letter == "e":
            first_digit += 1

    for letter in first_name_list:
        if letter == "l":
            second_digit += 1
        if letter == "o":
            second_digit += 1
        if letter == "v":
            second_digit += 1
        if letter == "e":
            second_digit += 1

    for letter in second_name_list:
        if letter == "t":
            first_digit += 1
        if letter == "r":
            first_digit += 1
        if letter == "u":
            first_digit += 1
        if letter == "e":
            first_digit += 1

    for letter in second_name_list:
        if letter == "l":
            second_digit += 1
        if letter == "o":
            second_digit += 1
        if letter == "v":
            second_digit += 1
        if letter == "e":
            second_digit += 1

    first_digit_str = str(first_digit)
    second_digit_str = str(second_digit)
    final_digit = first_digit+second_digit
    print(final_digit)
    print(f"love score of [ {first_name} ] and  [ {second_name} ] = ")


calculate_love_score("Naresh Kumar Verma", "Vinita Verma")


# print("love score of [ Anujeet Verma ] and [ Neha Ghosh ] = 100")