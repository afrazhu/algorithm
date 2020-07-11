#!/usr/bin/env python3
# https://leetcode-cn.com/problems/max-consecutive-ones/
# Given a binary array, find the maximum number of consecutive 1s in this array.
# 给定一个二进制数组， 计算其中最大连续1的个数。
# 中规中矩
binaryList = [1, 1, 1, 0, 1, 1, 1, 1]
num = 0
res = 0
for value in binaryList:
    if value == 1:
        num = num + 1
        res = max(res, num)
    else:
        num = 0
print(res)

# 其他操作
# 数组转字符串，用0分割，计算1的长度: https://leetcode-cn.com/u/vanshaw/
print(max(len(substr) for substr in ''.join([str(x) for x in binaryList]).split("0")))
