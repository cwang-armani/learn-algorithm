# -*- coding:utf-8 -*-
def prime_number(n):
    num = []
    for i in range(2,n+1):
        flag =0
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
            else:
                flag = 0
        if flag == 0:
            num.append(i)
    print(num)
a= prime_number(100)
