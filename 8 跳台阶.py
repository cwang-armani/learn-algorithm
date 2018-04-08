class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 0:
            return 1
        elif number <= 2:
            return number
        else:
            a,b = 1,2
            for i in range(2,number):
                a,b = b,a+b
            return b