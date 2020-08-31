#!/usr/bin/env python
# coding=utf-8
'''
Author: ReOneK
email: oneking1995@163.com
github: https://github.com/ReOnek
Date: 2020-08-31 19:48:36
'''

def permutation(nums):

    if len(nums)==1:
        return nums

    res=[]

    for i range(0,len(nums)):
        nums=nums[:i]+nums[i:]

        sub_per=permutation(nums)

        for j in sub_per:
            res.append(nums[i:i+1]+j)

    return res

