# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
            return False
        if len(pushV) == len(popV) == 0:
            return True
        
        list = []
        for temp in pushV:
            list.append(temp)
            # 必须先判断list中是否含有元素，否则在弹出最后一个元素后list[-1]已经不存在，报错list out of index
            while len(list) and list[-1] == popV[0]:
                list.pop()
                popV.pop(0)
        if list:
            return False
        else:
            return True