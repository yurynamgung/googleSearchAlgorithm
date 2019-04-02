#reads file into one array
def readFile(fileName):
    text_file = open(fileName, "r")
    lines = text_file.read().split()
    return lines

#splits array into two columns
def splitColumns(arr):
    col1 = [];
    col2 = [];
    for i in range(len(arr)):
        if (i%2) == 0:
            col1.append(arr[i])
        else:
            col2.append(arr[i])
    return col1, col2


list = readFile("web-Google.txt")
#print(list);
print(list[0])

col1, col2 = splitColumns(list)
print(col1[1])
print(col2[1])
