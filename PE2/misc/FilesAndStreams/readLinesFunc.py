try:
    s = open("/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/example.txt","rt")
    lines = s.readlines(10)
    counter = 0
    while lines != [ ]:
        print(lines)
        lines = s.readlines(10)
        counter += 1
    s.close()
except IOError as ioe:
    print(ioe)

lcnt = 0
#simpler and concise version of above code
try:
    for lines in open("/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/text.txt","rt"):
        lcnt +=1 
        print(lines)
except IOError as e:
    print(e)