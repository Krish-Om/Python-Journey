
from os import strerror

try:
    s = open("/home/krishom/Workspace/python/PE2/MIsc/example.txt",'rt')
    s.close()
except Exception as e:
    if e.errno == errno.ENONET:
        print("File don't exisits")
    elif e.errno == errno.EMFILE:
        print("You have opened too many files.")
    else:
        print("The error number is :", strerror(e.errno))
