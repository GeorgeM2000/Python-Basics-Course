if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    List = list(integer_list)
    t = ()
    for elem in List:
        temp_list = list(t)
        temp_list.append(elem)
        t = tuple(temp_list)
    
    print(hash(t))

    