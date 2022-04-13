import quicksort

def shellSort(nums):
    lens = len(nums)
    gap = 1
    while gap < lens // 3:  # // 表示整除，向下取整
        gap = gap * 3 + 1  # 动态定义间隔序列
    while gap > 0:
        print('gap = %s', gap)
        for i in range(gap, lens):
            curNum, preIndex = nums[i], i - gap  # curNum 保存当前待插入的数
            while preIndex >= 0 and curNum < nums[preIndex]:
                nums[preIndex + gap] = nums[preIndex] # 将比 curNum 大的元素向后移动
                preIndex -= gap
            nums[preIndex + gap] = curNum  # 待插入的数的正确位置
        gap //= 3  # 下一个动态间隔
    return nums

if __name__ == '__main__':
    array = [3, 5, 1, 9, 7, 0, 4, 2, 9, 3, 3, 4, 8, 1, 3, 5, 7, 10]
    shellSort(array)
    quicksort.output_sort(array)