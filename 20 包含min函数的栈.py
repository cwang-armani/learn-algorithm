# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.__item = []
    def push(self, node):
        # write code here
        self.__item.append(node)
    def pop(self):
        # write code here
        self.__item.pop()
    def top(self):
        # write code here
        return selt.__item[-1]
    def min(self):
        return min(self.__item)
        # write code here