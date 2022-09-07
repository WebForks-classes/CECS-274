import time
import numpy
start_time = time.time()

def sortByLengthLines(originalFile, destinationFile):
    ogfile = open(originalFile, 'r')
    lines = ogfile.readlines()

    arr = numpy.array(lines)
    arr_ = [len(x) for x in arr]
    x = arr[numpy.argsort(arr_)]

    dstfile = open(destinationFile, 'w')
    for i  in x:
        dstfile.write(i)

    dstfile.close()
    ogfile.close()

sortByLengthLines("originalFile.txt", "destinationFile.txt")
print("Process finished --- %s seconds ---" % (time.time() - start_time))
