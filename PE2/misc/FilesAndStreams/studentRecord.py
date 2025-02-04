# fileName = input("Enter the file name: ")
from os import strerror

file= "/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/samplefile.txt"

class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, *args):
        super().__init__(*args)
        print("No such files in Prof. Jellkyl's directory!!")
    # Write your code here.
        print("Bad line")
        exit(2)

class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__()
        print("The files content is empty!!!, this must not be the respective file.")
        exit(1)    
    # Write your code here.


data = {}

try:
    f = open(file,"rt")
    lines = f.readlines()
    f.close()

    for line in lines:
        columns = line.split()

        std = columns[0] + " " + columns[1]

        points = float(columns[2])

        try:
            data[std] += points
        except KeyError:
            data[std] = points
    
    for std in sorted(data.keys()):
        print(std,'\t',data[std])

except IOError as e:
    print(e)
except BadLine:
    print(BadLine)
except FileEmpty:
    print(FileEmpty)