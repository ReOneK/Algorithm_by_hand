#!/usr/bin/env python
# coding=utf-8
'''
Author: ReOneK
email: oneking1995@163.com
github: https://github.com/ReOnek
Date: 2020-08-31 09:57:18
'''


def permutations(arr, position, end):
    """
    调换法：对每一个位置分别固定，然后调换前后数据的位置得到全排列
    """
    if position == end:
        print(arr)
 
    else:
        for index in range(position, end):
 
            arr[index], arr[position] = arr[position], arr[index]
            print(arr)
            permutations(arr, position+1, end)
            arr[index], arr[position] = arr[position], arr[index]
            print(arr)
 
 
# arr = ["a","b","c"]
# permutations(arr, 0, len(arr))
    
    
    

    
