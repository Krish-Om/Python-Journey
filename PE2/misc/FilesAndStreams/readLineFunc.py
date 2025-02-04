from os import strerror

try:
    char_counter = line_counter = 0
    stream = open("/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/text.txt","rt")
    line = stream.readline()
    while line != "":
        line_counter += 1
        print(line)
        # for char in line:
        #     print(char, end="")
        #     char_counter += 1
        line = stream.readline()

    stream.close()
    print("\n\nCharacters in file: ",char_counter)
    print("Lines in file " ,line_counter)
except IOError as ioe:
    print(ioe)