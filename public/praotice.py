
def test(nums, x):
    index = 1

    for i in range(x):

        nums[index] = 1

        nums[index + 1] = 2

        index += 2

    return nums


if __name__ == '__main__':
    nums = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(test(nums, 3))