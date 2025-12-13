PLACEHOLDER = "[name]"

with open('./Input/Names/invited_name.txt') as names_file:
    name_list = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in name_list:
        new_letter = letter_contents.replace(PLACEHOLDER, name.strip())

        with open(f"./Output/ReadyToSend/{name.strip()}.txt", mode="w") as new_file:
            new_file.write(new_letter)