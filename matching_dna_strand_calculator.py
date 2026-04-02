input_user = input("Give me a strand of DNA (ATCG) to turn into its complementary strand:\n")
value = input_user.upper()
def DNA_Transformation(value_to_turn):
    new_value = ""
    for char in value_to_turn:
        if char == "A":
            char = "T"
            new_value += char
        elif char == "T":
            char = "A"
            new_value += char

        elif char == "C":
            char = "G"
            new_value += char

        elif char == "G":
            char = "C"
            new_value += char
        else:
            continue

    return(new_value)
print(DNA_Transformation(value))
