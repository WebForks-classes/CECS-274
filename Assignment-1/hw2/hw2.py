def removeDuplication(originalFile, destinationFile):

    #opens file and appends to list
    ogfile = open(originalFile, 'r')
    lines = ogfile.readlines()

    #creates list
    list = []
    a = 0
    i = lines[a]

    #removes duplicate or adds to list
    for i in lines:
        if i in list:
            lines.remove(i)
            a += 1
        else:
            list.append(i)
            a += 1

    #opens destination file and writes list to it
    dstfile = open(destinationFile, 'w')
    for item in list:
        dstfile.write(item)

    #closes files
    dstfile.close()
    ogfile.close()


removeDuplication("originalFile.txt", "destinationFile.txt")