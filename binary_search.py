#!/usr/bin/python

def binary_search(array, element):

    first = 0
    last = len(array) - 1
    found = False

    while first <= last and not found:

        mid = (first + last) / 2
        
        if array[mid] == element:
            found = True
        else:
            # left side of array
            if element < array[mid]:
                last = mid - 1
            # right side of array
            else:
                first = mid + 1
    
    return found

array = [1,2,3,4,5,6,7,8,9,10]
binary_search(array, 10)





