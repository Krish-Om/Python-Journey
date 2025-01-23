try:
    counter = 0
    stream = open("PE2/MIsc/FilesAndStreams/text.txt","rt")

    content = stream.read()
    for char in content:
        print(char,end='')
        counter+= 1
    stream.close()
    print("\n\nCharacters in file: ",counter)
except IOError as e:
    print(e)