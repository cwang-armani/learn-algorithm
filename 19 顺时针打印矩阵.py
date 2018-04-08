# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
    # write code here
        result = []
        while matrix:
            # 取出原矩阵 第一行 并删除
            result+=matrix.pop(0)
            if not matrix or not matrix[0]:
                break
                # 遍历列 取逆
            matrix = self.BackwardMatrix(matrix)
        return result

    def BackwardMatrix(self,matrix):
        row = len(matrix)
        col = len(matrix[0])
        new_matrix1 = []
        # 按列遍历
        for i in range(col):
            new_matrix2 = []
            for j in range(row):
                new_matrix2.append(matrix[j][i])
            new_matrix1.append(new_matrix2)
        # 逆序新矩阵
        return new_matrix1[::-1]