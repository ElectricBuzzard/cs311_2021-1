import random
import time

def min_index(a, i, j):
    if i == j:
        return i
    k = min_index(a, i + 1, j)

    if a[i]>a[k]:return i
    else:return k

def recursive_selection_sort(a, n, index=0):
    start_time=time.time()
    if index == n:
        print("--- %s seconds ---" % (time.time() - start_time))
        return -1
    k = min_index(a, index, n - 1)
    if k != index:
        a[k], a[index] = a[index], a[k]
    recursive_selection_sort(a, n, index + 1)
   # print("--- %s seconds ---" % (time.time() - start_time))

nums = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
data_length = len(nums)

print('Before sorting',nums)
recursive_selection_sort(nums, data_length)
print('After sorting ',nums)

def bubbleSort(a):
    start_time=time.time()
    n = len(a)
    for i in range(n):
        for j in range(1, n-i, +1):
            if a[j-1] > a[j]:
                t = a[j]
                a[j]=a[j-1]
                a[j-1] =t
    print("--- %s seconds ---" % (time.time() - start_time))



a = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]

print("before",a)
bubbleSort(a)
print("after",a)







