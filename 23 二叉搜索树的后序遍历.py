# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # 递归无返回结果
        if len(sequence) == 0:
            return False
        # 已经查到了最后一个元素
        if len(sequence) == 1:
            return True
        # 根节点
        root = sequence[-1]
        i = 0
        # 找到第一个比根节点大的值的索引
        for temp in sequence[:-1]:
            if temp > root:
                break
            i += 1
        # 判断索引右侧序列
        for temp in sequence[i:-1]:
            if temp < root:
                return False
        # 迭代索引左右子树
        return self.VerifySquenceOfBST(sequence[:i]) or self.VerifySquenceOfBST(sequence[i:-1])