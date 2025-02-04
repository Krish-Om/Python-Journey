from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10+i
print(tuple(data))

try:
    bf = open("/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/byteArrayEx.bin","wb")
    bf.write(data)
    bf.close()
except IOError as e:
    print(e)

data2 = bytearray(10)
try:
    bf = open("/home/krishom/Workspace/python/PE2/MIsc/FilesAndStreams/byteArrayEx.bin","rb")
    bf.readinto(data2)
    bf.close()

    for b in data:
        print(hex(b), end=" ")
except IOError as e:
    print(e)
