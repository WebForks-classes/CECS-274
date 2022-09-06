import time
start_time = time.time()

def sortByLengthLines(originalFile, destinationFile):
    
    #opens files
    ogfile = open(originalFile, 'r')
    lines = ogfile.readlines()
    list = lines

    #bubble sort
    n = len(list)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if len(list[j]) > len(list[j+1]):
                swapped = True
                list[j], list[j+1] = list[j+1], list[j]
        if not swapped:
            return

    #writes list to destination file
    dstfile = open(destinationFile, 'w')
    for item in list:
        dstfile.write(item)  

    #closes files
    dstfile.close()
    ogfile.close()

sortByLengthLines('originalFile.txt', 'destinationFile.txt')
print("Process finished --- %s seconds ---" % (time.time() - start_time))