def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot 
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

            # pivot = arr[high]，将 pivot 放置在中间位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    # low = high 说明只有一个元素，无需比较
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def output_sort(arr):
    """output the sorted array"""
    print('排序后的数组：')
    for i in range(len(arr)):
        print(arr[i], end=' ')


'''非递归版本 （区别仅为Qsort方法，使用栈来保存中间结果），python3 执行
'''

def swap(lst, left, right):
    lst[left], lst[right] = lst[right], lst[left]


def sort_paritition(lst, left, right):
    key = lst[left]
    while left < right:
        if left < right and key <= lst[right]:
            right = right - 1
        swap(lst, left, right)

        if left < right and lst[left] <= key:
            left = left + 1
        swap(lst, left, right)
    print('left: {} right: {} lst: {}'.format(left, right, lst))
    return left


def Qsort(lst, left, right):
    piviots = [(left, right)]
    while len(piviots) > 0:
        piviot = piviots.pop(0)
        if piviot[0] < piviot[1]:
            piviot_num = sort_paritition(lst, piviot[0], piviot[1])
            # piviot_num = partition(lst, piviot[0], piviot[1])

            if piviot_num - 1 > piviot[0]:
                piviots.append((piviot[0], piviot_num-1))

            if piviot_num + 1 < piviot[1]:
                piviots.append((piviot_num+1, piviot[1]))


def Quicksort(lst):
    Qsort(lst, 0, len(lst) - 1)


if __name__ == '__main__':
    arr = [5, 3, 8, 9, 1, 5]
    n = len(arr)
    Quicksort(arr)
    #quickSort(arr, 0, n - 1)
    print("排序后的数组:")
    output_sort(arr)
