# what it does ?
# it picks the first two elements of a list and compare them for the lowest value
# then it keeps the lowest value at the begining always
# and so on it keeps checking pair by pair


import sys

a = [64,25,12,22,11]

for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if a[min_index]>a[j]:
            min_index = j

    a[i],a[min_index] = a[min_index],a[i]
print(a)


# coded By biswas Sampad Satpathy
