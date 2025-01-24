file = input("Enter the file name: ")
filePath = "/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/"+file

histogram = {}
try:
    stream = open(filePath,"rt")
    content = stream.read().lower()
    for char in content:
        if char.isalpha():
            if char in histogram.keys():
                histogram[char] += 1
            else:
                histogram[char] = 1
    stream.close()
except Exception as e:
    print(e)
print(sorted(histogram))
print(histogram)
