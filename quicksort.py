'''
快速排序
大O运行时间：O(n log n)
快速排序的速度取决于选择的基准值
'''
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1,4,2,66,32,3,77,13,25,36,57,8]))
