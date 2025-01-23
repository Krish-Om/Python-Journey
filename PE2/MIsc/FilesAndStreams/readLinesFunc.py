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