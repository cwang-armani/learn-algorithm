# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.item = []
    def push(self, node):
        # write code here
        return self.item.append(node)
    def pop(self):
        # return xx
        return self.item.pop(0)