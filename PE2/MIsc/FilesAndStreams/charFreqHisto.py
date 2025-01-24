
def sortHistogram(histogram):
    sortedHistogram ={}
    keys = sorted(histogram.keys())
    for k in keys:
        print(histogram[k])
        sortedHistogram[k]= histogram[k]
    return sortedHistogram


def sortWithFreq(histogram):
    newHistoGram = {}
    for c in sorted(histogram.keys(), key=lambda x:histogram[x], reverse=True):
        newHistoGram[c] = histogram[c]

    return newHistoGram


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
new = (sortWithFreq(histogram))

try:
    newFile = open(filePath + '.hist', "wt+")
    for ch in new.keys():
        str = ch +" -> " + f"{new[ch]}" +"\n"
        newFile.write(str)
    newFile.close()
except Exception as e:
    print(e)



