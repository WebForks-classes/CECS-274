def sortByLengthLines(originalFile, destinationFile):
    
    ogfile = open(originalFile, 'r')
    lines = ogfile.readlines()
    list = lines


    n = len(list)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if len(list[j]) > len(list[j+1]):
                swapped = True
                list[j], list[j+1] = list[j+1], list[j]
        if not swapped:
            return

    dstfile = open(destinationFile, 'w')
    for item in list:
        dstfile.write(item)  
  
    dstfile.close()
    ogfile.close()
sortByLengthLines('originalFile.txt', 'destinationFile.txt')