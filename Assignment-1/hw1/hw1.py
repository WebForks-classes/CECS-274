def reverse(originalFile, destinationFile):
    #opens the original file and turns lines in original file into a list
    ogfile = open(originalFile, 'r')
    lines = ogfile.readlines()

    #creates a new list and reverses the order of the lines in the original file
    list = []
    while len(lines) > 0:
        list.append(lines.pop())

    #opens the destination file and writes the reversed lines to the destination file
    dstfile = open(destinationFile, 'w')
    for item in list:
        dstfile.write(item)

    #closes the files   
    dstfile.close()
    ogfile.close()

reverse("originalFile.txt", "destinationFile.txt")