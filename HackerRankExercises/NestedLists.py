def lowestGradeStudents(arr):
    # Sort the nested list based on the student scores
    arr.sort(key=lambda x:x[1])

    # Delete lowest duplicate values
    count = 0
    while arr[0][1] == arr[1][1] and count != len(arr)-1:
        arr.remove(arr[1])
        count += 1

    if count == len(arr)-1:
        print(arr[0][0])
    else:
        arr.remove(arr[0])  # Delete the lowest score student

        # Store second lowest student names
        lowest_grade_student_name_list = [arr[0][0]]
        for i in range(1, len(arr)):
            if arr[i][1] == arr[0][1]:
                lowest_grade_student_name_list.append(arr[i][0])
        
        lowest_grade_student_name_list.sort()
        print(lowest_grade_student_name_list)


if __name__ == '__main__':
    List = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        temp_list = [name, score]
        List.append(temp_list)

    lowestGradeStudents(List)

