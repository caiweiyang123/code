"""
1. 排序的概念
什么是排序：所谓排序，就是使一串记录按照其中的某个或某些关键字的大小，按递增或递减方式排列起来的操作。

排序的稳定性：假定在待排序的记录序列中存在多个具有相同的关键字的记录，若经过排序，这些记录的相对次序保持不变，
即在原序列中，r[i]=r[j]，且r[i]在r[j]之前，而在排序后的序列中，r[i]仍在r[j]之前，则称这种排序算法是稳定的；否则称为该排序算法是不稳定的。
"""
# 1. 直接插入排序
"""
1.1 排序思想
直接插入排序是一种简单的插入排序法，其基本思想是：把待排序的记录按其关键码值的大小逐个插入到一个已经排好序的有序序列中，直到所有的记录插入完为止，得到一个新的有序序列 。
"""


def insertion_sort(arr):
    # 遍历数组
    for i in range(1, len(arr)):
        key = arr[i]  # 当前待插入的元素
        j = i - 1  # 从当前元素的前一个位置开始比较
        # 将比 key 大的元素向右移动
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # 将 key 插入到正确的位置


# 2. 希尔排序
"""
2.1 排序思想
希尔排序法又称缩小增量法，也是插入排序的一种，是对直接插入排序的优化。希尔排序法的基本思想是：
先选定一个整数，把待排序文件中所有记录分成 gap 个组，所有距离为 gap 的记录分在同一组内，并对每一组内的记录进行直接插入排序，
然后重复上述分组和排序的工作，当全部分组都进行排序后，最后再整体进行一次直接插入排序，使得文件内所有记录达到有序.
"""


def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初始化间隔

    # 不断缩小间隔直到为1
    while gap > 0:
        # 从间隔开始遍历数组
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 对间隔步长的子数组进行插入排序
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        # 缩小间隔
        gap //= 2


# 3. 直接选择排序
"""
3.1 排序思想
直接选择排序即每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，
直到全部待排序数据元素排完；这里我们对其做一些简单的优化 – 每次选两个数，选出最小的放在最前面，选出最大的放在最后面。
"""


def selection_sort(arr):
    # 遍历整个数组
    for i in range(len(arr)):
        # 初始化最小元素的索引
        min_index = i

        # 在未排序部分找到最小元素的索引
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
        
        

        # 将找到的最小元素与当前位置交换
        arr[i],arr[min_index] = arr[min_index],arr[i]

# 4. 堆排序
"""
4.1 排序思想
堆排序 (Heapsort) 是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种；
它通过堆来进行选择数据；需要注意的是排升序要建大堆，排降序建小堆。
"""
def heapify(arr, n, i):
    largest = i  # 初始化父节点索引为最大值
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # 检查左子节点是否存在且大于父节点
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    # 检查右子节点是否存在且大于父节点或左子节点
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # 如果最大值不是父节点，则交换父节点和最大值节点，并递归调整堆
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个个取出堆顶元素，再调整堆
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# 5. 冒泡排序
"""
5.1 排序思想
交换排序基本思想：所谓交换，就是根据序列中两个记录键值的比较结果来对换这两个记录在序列中的位置。
交换排序的特点是：将键值较大的记录向序列的尾部移动，键值较小的记录向序列的前部移动。
"""
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]> arr[j]:
                arr[i],arr[j] = arr[j],arr[i]


# 6. 快速排序
"""
6.1 排序思想
快速排序是 Hoare 于1962年提出的一种二叉树结构的交换排序方法，
其基本思想为：任取待排序元素序列中的某元素作为基准值，按照该排序码将待排序集合分割成两子序列，
左子序列中所有元素均小于基准值，右子序列中所有元素均大于基准值，然后最左右子序列重复该过程，直到所有元素都排列在相应位置上为止。

"""
#递归版
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # 小于基准值的元素放在左边，大于基准值的元素放在右边
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        # 递归地对左右两部分进行快速排序
        return quick_sort(left) + [pivot] + quick_sort(right)

# 指针版
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

if __name__ == '__main__':
    # 示例
    arr = [64, 34, 25, 12, 22, 11, 90]
    selection_sort(arr)
    print("排序后的数组：", arr)
