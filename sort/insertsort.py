import quicksort

def insertionSort(nums):
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        curNum, preIndex = nums[i+1], i  # curNum 保存当前待插入的数
        while preIndex >= 0 and curNum < nums[preIndex]: # 将比 curNum 大的元素向后移动
            nums[preIndex + 1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex + 1] = curNum  # 待插入的数的正确位置
    return nums

if __name__ == '__main__':
    array = [3, 5, 1, 4, 7, 10, 1, 2, 1, 3]
    insertionSort(array)
    quicksort.output_sort(array)