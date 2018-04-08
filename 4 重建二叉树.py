# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            # 前序遍历的第一个元素即为根节点
            binary_tree = TreeNode(pre[0])
            # 找到根节点在中序遍历中的索引
            mid_index = tin.index(pre[0])
            # 前序递归中 左子树、右子树的第一个节点仍然是根节点
            binary_tree.left = self.reConstructBinaryTree(pre[1:mid_index+1],tin[:mid_index])
            binary_tree.right = self.reConstructBinaryTree(pre[mid_index+1:],tin[mid_index+1:])
            return binary_tree