import quicksort

def selectionSort(nums):
    for i in range(len(nums) - 1):  # 遍历 len(nums)-1 次
        minIndex = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minIndex]:  # 更新最小值索引
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i] # 把最小数交换到前面
    return nums

if __name__ == '__main__':
    array = [3, 5, 1, 4, 7, 10, 1, 2, 1, 3]
    selectionSort(array)
    quicksort.output_sort(array)
