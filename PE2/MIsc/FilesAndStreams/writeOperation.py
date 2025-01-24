try:
    file = open("/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/writingOpe.txt","a")
    for i in range(10):
        file.write("line no. "+str(i+1) + "\n")
    file.close()
except IOError as e:
    print(e)