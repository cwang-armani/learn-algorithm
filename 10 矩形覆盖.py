# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <=2:
            return number
        else:
            a,b=1,2
            for i in range(2,number):
                a,b = b,a+b
            return b