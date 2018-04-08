# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        result = ''
        for temp in s:
            if temp == ' ':
                result += '%20'
            else:
                result += temp
        return result