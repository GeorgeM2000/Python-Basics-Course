if __name__ == '__main__':
    n = int(input())

    # Take an input and convert it from a string to an int value.
    arr = map(int, input().split()) 

    List = list(arr)

    List.sort(reverse=True)

    runnerUpScore = None
    count = 0
    while(List[1] == List[0] and count != len(List)-1):
        List.remove(List[1])
        count += 1

    if count == len(List)-1:
        runnerUpScore = List[0]
    
    runnerUpScore = List[1]
        

    print(runnerUpScore)


