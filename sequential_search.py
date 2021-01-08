#!/usr/bin/python

def seq_search(array, element):

    position = 0
    # will return true if our match is found
    found = False

    while position < len(array) and not found:
        
        if array[position] == element:
            found = True

        else:
            position += 1

        return found

array = [1,2,3,4,5]
print(seq_search(array, 6))

def ordered_seq_search(array, element):

    position = 0
    found = False
    stopped = False

    while position < len(array) and not found and not stopped:
        
        if array[position] == element:
            found = True

        else:
            
            if array[position] > element:
                stopped = True
            else:
                position += 1

        return found

print(ordered_seq_search(array, 3))

