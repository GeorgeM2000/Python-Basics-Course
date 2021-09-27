"""
    Write a Python program to find the key of the maximum and minimum value in a dictionary
"""

if __name__ == "__main__":
    dict = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}


    key_list = list(dict.keys())
    val_list = list(dict.values())

    max = val_list[0]
    min = val_list[0]
    for key,value in dict.items():
        if value > max: max = value
        if value < min: min = value
    

    
    print(f'Maximum : {key_list[val_list.index(max)]}')
    print(f'Minimum : {key_list[val_list.index(min)]}')
