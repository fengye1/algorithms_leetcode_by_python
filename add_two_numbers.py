# coding:utf-8
# @Time    : 2017/12/1 19:28
# @Author  : lvpf
# @File    : add_two_numbers.py

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num=0
        for i in range(len(l1)):
            num += l1[i]*10**i+l2[i]*10**i
        return num

if __name__ == '__main__':
    num = Solution().addTwoNumbers([2, 4, 3], [5, 6, 4])
    print list(str(num))[::-1]