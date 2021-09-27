def split(string):
    return [char for char in string]


def parseString(string, function):
    if function == "isalnum":
        for char in splited_string: 
            if char.isalnum(): return True
        return False
    elif function == "isalpha":
        for char in splited_string: 
            if char.isalpha(): return True
        return False
    elif function == "isdigit":
        for char in splited_string: 
            if char.isdigit(): return True
        return False
    elif function == "islower":
        for char in splited_string: 
            if char.islower(): return True
        return False
    elif function == "isupper":
        for char in splited_string: 
            if char.isupper(): return True
        return False

if __name__ == '__main__':
    s = input()


    splited_string = split(s)

    print(parseString(splited_string, "isalnum"))
    print(parseString(splited_string, "isalpha"))
    print(parseString(splited_string, "isdigit"))
    print(parseString(splited_string, "islower"))
    print(parseString(splited_string, "isupper"))

    
    