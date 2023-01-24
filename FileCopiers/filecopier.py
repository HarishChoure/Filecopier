import os

def filecopy(fileName):
   
    copiedFile = fileName

    file_name, file_extension = os.path.splitext(copiedFile)
    i = 1
    new_file = file_name + " - Copy" + file_extension

    while os.path.isfile(new_file):
        new_file = file_name + " - Copy (" + str(i) + ")" + file_extension
        i += 1
    with open(copiedFile, 'rb') as in_file, open(new_file, 'wb') as out_file:
        out_file.write(in_file.read())
    print("Successfully file is copied  " + new_file)


if __name__ == '__main__':

    path = 'C:/Users/Harish Choure/PycharmProjects/FileCopiers'
    files_list = os.listdir(path)

    print("Files in myFiles Directory:")
    for x in files_list:
        print(x)

    fileName = input("Enter the name of the file that you want to copy ")
    print(fileName)

    isPresent = False
    count = 0
    for file in files_list:
        if (file == fileName):
            isPresent = True
            break

    if (isPresent):
        filecopy(fileName)
    else:
        print("File does not exist ")
