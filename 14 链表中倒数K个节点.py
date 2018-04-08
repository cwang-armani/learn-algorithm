# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k<=0 and head is None:
            return None
        else:
            count = 0
            pre = head
            cur = head
            while pre is not None:
                pre = pre.next
                count +=1
                if count>k:
                    cur = cur.next
            if count<k:
                return None
            return cur