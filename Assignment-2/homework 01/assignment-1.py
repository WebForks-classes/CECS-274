
def merge_playlist(insert, second_list):
    first_list[insert:insert] = second_list
    print(first_list)



def main():
    first_list = []
    second_list = []


first_list = [1, 2, 3, 4]
second_list = [5,6,7]  
merge_playlist(2, second_list)

#running time big o notation is O(n) because the running time is directly proportional to the size of the input
#It is not efficent to implement add_all(i;c) because if we want to add more elements that the array can not support it will
#take more time and more resources to do so.