#!/usr/bin/python

def rec_bin_search(array, element):

    if len(array) == 0:
        return False

    else:
        mid = len(array) / 2
    
    if array[mid] == element:
        return True

    else:
        if element < array[mid]:
            return rec_bin_search(arr[:mid], element)

        else:
            return rec_bin_search(arr[mid + 1:], element)

