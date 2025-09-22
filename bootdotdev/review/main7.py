def join_strings(strings):
    new_string = ""
    for string in strings:
        if new_string == "":
            new_string = string
        else:
            new_string += "," + string
    return new_string
