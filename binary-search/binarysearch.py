# Let's trie to prove that binary search is faster than the naive search.

# The naive search we have to iterate over the whole list to find the element.
import random
import time


def naive_search(list, target):
    for index in range(len(list)):
        if list[index] == target:
            return index
    return -1

# The binary search is a divide and conquer algorithm.
# that means we will leverage the fact that our list is SORTED.
def binary_search(list, target, lowest_index=None, highest_index=None):
    if lowest_index is None:
        lowest_index = 0
    if highest_index is None:
        highest_index = len(list) - 1
    
    if lowest_index > highest_index:
        return -1
    
    midpoint = (lowest_index + highest_index) // 2
    
    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, lowest_index, midpoint - 1)
    else:
        return binary_search(list, target, midpoint + 1, highest_index)
    
if __name__ == '__main__':
    # Let's create a list of random numbers.
    length = 10000
    # build a list of random numbers from 0 to length
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))
    
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print(f'Naive search took {(end - start)/length} seconds')
    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print(f'Binary search took {(end - start)/length} seconds')
