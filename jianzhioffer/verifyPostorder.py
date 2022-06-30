class Solution:
    # 二叉搜索树 = 二叉排序树，左结点 < 根结点 < 右结点
    def verifyPostorder(self, postorder: list) -> bool:

        length = len(postorder)

        if length == 1 or length == 0:
            return True

        root = postorder[-1]
        postorder = postorder[:-1]

        split_index = None

        left_val = []
        right_val = []
        left_result = right_result = False

        for i in range(len(postorder) - 1, -1, -1):

            if postorder[i] < root:
                if split_index is None:
                    split_index = i
                left_val.insert(0, postorder[i])
            else:
                if split_index and i < split_index:
                    return False
                right_val.insert(0, postorder[i])

        left_result = self.verifyPostorder(left_val)
        right_result = self.verifyPostorder(right_val)

        return left_result and right_result


if __name__ == "__main__":
    s = Solution()

    for postorder, result in [
        ([1, 6, 3, 2, 5], False),
        ([1, 3, 2, 6, 5], True),
        ([1, 2, 5, 10, 6, 9, 4, 3], False),
        (
            [
                179,
                437,
                1405,
                5227,
                8060,
                8764,
                8248,
                4687,
                3297,
                13038,
                12691,
                15744,
                16195,
                15642,
                19813,
                17128,
                21051,
                20707,
                22177,
                21944,
                23644,
                23281,
                19970,
                23652,
                26471,
                31467,
                33810,
                32300,
                33880,
                27334,
                25987,
                35643,
                35103,
                36489,
                42534,
                42990,
                42942,
                37090,
                36075,
                34516,
                16624,
                11335,
                10737,
                44641,
                45754,
                47096,
                46021,
                49150,
                48013,
                49814,
                51545,
                52555,
                50701,
                47875,
                56783,
                57558,
                53812,
                62008,
                61737,
                63052,
                63478,
                62799,
                59246,
                64765,
                64066,
                63862,
                65384,
                67449,
                66552,
                57741,
                45618,
                44412,
                667,
                69718,
                75519,
                76819,
                72971,
                79319,
                78145,
                80615,
                84280,
                80984,
                86598,
                85903,
                84334,
                80867,
                87993,
                92361,
                88465,
                87738,
                80364,
                94380,
                94446,
                96785,
                93694,
                76847,
                99655,
                98675,
                97001,
                72112,
            ],
            True,
        ),
    ]:

        print("计算结果: %s, 预期结果: %s" % (s.verifyPostorder(postorder), result))
