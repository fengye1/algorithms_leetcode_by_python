# coding:utf-8
# @Time    : 2017/12/1 18:35
# @Author  : lvpf
# @File    : 01two_sum.py
class Solution(object):
    """
    找出数组numbers中的两个数，它们的和为给定的一个数target，并返回这两个数的索引，
    """

    def twoSum1(self, nums, target):
        """for 循环两次"""
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j:
                    if (nums[i] + nums[j]) == target:
                        return i, j

    def twoSum(self, nums, target):
        """for循环，将值存到key中，"""
        dict_a = {}
        for i, num in enumerate(nums):
            if target-num in dict_a.keys():
                return dict_a[target-num], i
            dict_a[num] = i



if __name__ == '__main__':
    value = Solution().twoSum([3, 2, 4], 6)
    print value