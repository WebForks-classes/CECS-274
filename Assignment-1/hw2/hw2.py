def removeDuplication(originalFile, destinationFile):
    a = 1
    list = {}
    ogfile = open(originalFile, 'r')
    for lines in ogfile:
        list[lines] = a
        a = a + 1
    ogfile.close()


    dstfile = open(destinationFile, 'w')
    for item in list:
        dstfile.write(item)

removeDuplication("originalFile.txt", "destinationFile.txt")