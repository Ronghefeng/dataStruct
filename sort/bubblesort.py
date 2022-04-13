import quicksort

def bubbleSort(nums):
    for i in range(len(nums) - 1): # 遍历 len(nums)-1 次
        for j in range(len(nums) - i - 1): # 已排好序的部分不用再次遍历
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == '__main__':
    array = [3, 5, 1, 4, 7, 10, 1, 2, 1, 3]
    bubbleSort(array)
    quicksort.output_sort(array)
