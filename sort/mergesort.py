import quicksort


def merge(left, right):
    # 归并过程
    result = []  # 保存归并后的结果
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result = result + left[i:] + right[j:]  # 剩余的元素直接添加到末尾
    return result

def mergeSort(nums):
    # 递归过程
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

if __name__ == '__main__':
    array = [3, 5, 1, 9, 7, 0, 4, 2, 9, 3, 3, 4, 8, 1, 3, 5, 7, 10]
    mergeSort(array)
    quicksort.output_sort(array)