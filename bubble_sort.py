#!/usr/bin/python

def bubble_sort(array):
    
    for n in range(len(array) - 1, 0, -1):
        for k in range(n):

            if array[k] > array[k+1]:
                temp = array[k]
                array[k] = array[k + 1]
                array[k + 1] = temp

array = [5,3,7,2]
bubble_sort(array)
print(array)
