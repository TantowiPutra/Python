# File Not Found

try:
    # with open("a.file.txt") as file:
    #     file.read()

    # Raise Custom Error
    raise ValueError("This is custom error")
except FileNotFoundError:
    print("There was an error")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    # file.close()
    print("File was closed.")