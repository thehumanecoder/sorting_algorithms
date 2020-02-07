import sys

def bubblesort(array):
    n = len(array)
    print('Original Array',array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                print(array)

    return array


arr = [64,34,25,12,22,11,90]
sorted_array = bubblesort(arr)
print("Sorted Array",sorted_array)
