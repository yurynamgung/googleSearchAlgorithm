##Yury Namgung and Hannah Davalos: Numerical Linear Algebra
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


#array 1:outsourcing link
#array 2:links to other things
from array import *

my_array1 = array('i', [1,2,3,4,5,6,7,8,9,10])
my_array2 = array('i', [1,2,5,11,22,33,44,77])
my_array3 = array('i', [1,2,3,4,5,6,7,8,9,10])
my_array4 = array('i', [40,50,60,11,22,33,44,77])
my_array5 = array('i', [1,2,3,4,5,6,7,8,9,10])

def elementsInCommon(array1, array2):
    i = 0
    for i in range(len(array2)):
        if array2[i] not in array1:
            print(i, array2[i])
    print("These are dangling nodes.")


#subwebs not connected to any other things
#assuming that there are no dangling nodes
