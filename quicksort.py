'''
快速排序
大O运行时间：O(n log n)
快速排序的速度取决于选择的基准值
'''
def quicksort(array):
    #基线条件：空，或者只有一个元素的数组是‘有序’的
    if len(array) < 2:
        return array
    else:
        #递归条件
        #基准值固定为数组中第一个元素
        pivot = array[0]
        #由所有小于基准值的元素构成的子数组
        less = [i for i in array[1:] if i <= pivot]
        #由所有大于基准值的元素构成的子数组
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([1,4,2,66,32,3,77,13,25,36,57,8]))


#使用随机数
import random

def quicksort(array):
    #基线条件：空，或者只有一个元素的数组是‘有序’的
    if len(array) < 2:
        return array
    else:
        #基准值为数组中随机位置的元素
        index = int(random.randint(0,(len(array)-1)))
        pivot = array[index]
        #弹出数组中的基准值，然后进行分区
        array.pop(index)
        #由所有小于基准值的元素构成的子数组
        less = [i for i in array if i <= pivot]
        #由所有大于基准值的元素构成的子数组
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,66,32]))


#采用二分法的快速排列（基准值为中间元素）
def quicksort(array):
    #基线条件：空，或者只有一个元素的数组是‘有序’的
    if len(array) < 2:
        return array
    else:
        #基准值为数组中的中间元素
        index = int(len(array)/2)
        pivot = array[index]
        #弹出数组中的基准值，然后进行分区
        array.pop(index)
        #由所有小于基准值的元素构成的子数组
        #less or greater 中的判断语句中必须有（且只能有）一个‘=’号，不然无法显示重复元素
        less = [i for i in array if i <= pivot]
        #由所有大于基准值的元素构成的子数组
        greater = [i for i in array if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,66,32]))
