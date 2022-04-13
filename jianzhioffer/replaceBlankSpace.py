
class Solution:
    def replaceSpace(self, s):
        # spilt_str = s.split(' ')
        # s = '%20'.join(spilt_str)
        # return s
        return s.replace(' ', '%20')

if __name__ == '__main__':
    str = 'We are happy.'
    solution = Solution()
    result = solution.replaceSpace(str)
    print(result)