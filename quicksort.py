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
    if len(array) < 2:
        print("小于2 return")
        return array
    else:
        index = int(random.randint(0,len(array)-1))
        pivot = array[index]
        print("index:",index,"pivot:",pivot)
        less = [i for i in array[:] if i < pivot]

        print("less",less)

        greater = [i for i in array[:] if i > pivot]

        print("greater",greater)
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,5,2,66,32]))
