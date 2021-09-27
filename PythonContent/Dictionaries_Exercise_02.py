"""
    Write a Python script to sort (ascending or descending) a dictionary by value
"""


def getKey(valueNum, dict):
    for key,value in dict.items():
        if value == valueNum:
            return key

if __name__ == "__main__":
    dict = {0:23, 1:2, 2:30, 3:45, 4:17, 5:6, 6:50}

    val_list = list(dict.values())
    val_list.sort()

    temp_dict = {}
    i = 0
    for i in range(len(dict)):
        temp_dict[getKey(val_list[i], dict)] = val_list[i]
        i += 1
    
    dict = temp_dict.copy()

    print(dict)