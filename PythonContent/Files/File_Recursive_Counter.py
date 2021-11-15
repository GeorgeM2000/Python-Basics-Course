import os


def file_counter(path):
    count = 0
    for file in os.listdir(path):
        if os.path.isdir(path + "\\" +  file):
            new_path = path + "\\" +  file
            print(new_path)
            count += file_counter(new_path)
        else:
            count += 1

    return count
            

if __name__ == "__main__":
    folder_path = input("Enter the folder path (C:\\path\\to\\file) : ")
    print("Files : " + str(file_counter(folder_path)))

