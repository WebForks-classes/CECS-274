import numpy
import array

class List:
    @staticmethod
    def list(list):
        global arr
        arr = numpy.array(list)
        print(arr)
    def size(list):
        global arr
        print(numpy.size(arr))
    def get(index):
        global arr
        result = numpy.where(arr == index)
        print(result[0], sep='\n')
        return result[0]
    def set(index, value):
        global arr
        arr[index] = value
        print(arr)
    def add(index, value):
        global arr
        arr = numpy.insert(arr, index, value)
        print(arr)
    def remove(index):
        global arr
        arr = numpy.delete(arr, index)
        print(arr)

class USet:
    @staticmethod
    def set(set):
        global my_set
        arr2set = numpy.array(set)
        my_set = numpy.unique(arr2set)
        print(my_set)
    def size(list):
        global my_set
        print(numpy.size(my_set))
    def add(index, value):
        global my_set
        my_set = numpy.insert(my_set, index, value)
        print(my_set)
    def remove(index):
        global my_set
        my_set = numpy.delete(my_set, index)
        print(my_set)
    def find(value):
        global my_set
        if value in my_set:
            print(value)
        else:
            print("None")

class Ssort:
    @staticmethod
    def set(set):
        global my_set
        arr2set = numpy.array(set)
        my_set = {e for l in arr2set for e in l}
    def size(list):
        global my_set
        print(numpy.size(my_set))
    def add(index, value):
        global my_set
        my_set = numpy.insert(my_set, index, value)
        print(my_set)
    def remove(index):
        global my_set
        my_set = numpy.delete(my_set, index)
        print(my_set)
    def find(value):
        global my_set
        if value in my_set:
            a = numpy.mininum(my_set)
            print(a)
        else:
            print("None")
