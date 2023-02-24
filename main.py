import timeit
from algorithms import SearchingAlgorithms

if __name__ == '__main__':
    #  For Using Binary Search 'seq' should be sorted
    seq = [1, 2, 3, 4]
    element = 40
    start = timeit.default_timer()
    found = SearchingAlgorithms().BinarySearch(seq=seq, element=element)
    if found:
        print("Element Found...!")
    else:
        print("Element Not Found...!")
    stop = timeit.default_timer()
    print('Binary Search Taken Time: ', stop - start)
