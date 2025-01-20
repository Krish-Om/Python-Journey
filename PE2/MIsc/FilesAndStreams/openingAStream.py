try:
    stream = open("/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/example.txt","rt")
    print(stream.readline())
    print("Successfully opened example.txt")
    stream.close()

except Exception as e:
    print(e)

