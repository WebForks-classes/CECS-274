import numpy
import array


#q1 using list interface

#q2 using USet interface 26275
def removeDuplication(originalFile, destinationFile):
    ogfile = open(originalFile, 'r')
    lines = ogfile.readlines()

    ogset = set()
    a = 0
    i = lines[a]

    for i in lines:
        ogset.add(i)
        a += 1
    
    dstfile = open(destinationFile, 'w')
    for item in ogset:
        dstfile.write(item)
    
    dstfile.close()
    ogfile.close()

removeDuplication("originalFileQ2.txt", "destinationFileQ2.txt")
