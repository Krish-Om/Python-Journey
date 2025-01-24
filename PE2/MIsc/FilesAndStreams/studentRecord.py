# fileName = input("Enter the file name: ")
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
lines =[]
students = []
data = {}
try:
    stream = open(file, "rt")
    for line in stream.readlines():
        lines.append(line.split())
        # lines.pop()
    print(lines)
    for s in lines:
        name = s[0]+" "+s[1]
        score = float(s[2])
        if name in data.keys():
            data[name]=score+float(s[2])
        data[name] = score
        
    print(data)
    stream.close()
except BadLine:
    print(BadLine)
except FileEmpty:
    print(FileEmpty)
except IOError as e:
    print(e)
    


