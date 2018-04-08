# -*- coding:utf-8 -*-
class Solution(object):
    # array 二维列表
    def Find(self, target, array):
        # write code here
        flag = False
        for index in range(len(array)):
            if target in array[index]:
                flag = True
        return flag