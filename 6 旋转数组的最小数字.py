# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)
        if n == 0:
            return 0
        for i in range(1,n):
            if rotateArray[i]<rotateArray[i-1]:
                return rotateArray[i]