'''
Author: sk 2309620371@qq.com
Date: 2023-02-04 12:23:17
LastEditors: sk 2309620371@qq.com
LastEditTime: 2023-02-06 11:12:39
FilePath: \python_code\力扣刷题\二分查找.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

nums = [-1,0,3,5,9,12]
target = 1


def search(nums,target,low,high):
    print('[low,high]',low,high)
    mid = (low + high) // 2
    print('mid: ',mid)
    if  low > high:
        print("退出")
        return -1
    if nums[mid] == target:
        print("等于")
        return mid
        print("end")
    elif nums[mid] < target:
        print("大于")
        search(nums,target,mid+1,high)
    elif nums[mid] > target:
        print("小于")
        search(nums,target,low,mid-1)

# search(nums,target,0,len(nums)-1)

# ! 版本2 可以找到元素，但索引无法回溯给return
def search2(nums,target):
    if (len(nums)-1) < 0:
        # print("退出")
        return -1
    # print("[low:high]",0,len(nums)-1)

    mid = len(nums) // 2
    # print('mid: ',mid)

    if nums[mid] == target:
        # print("等于")
        return mid
    elif nums[mid] < target:
        # print("大于")
        # print("[low:high]",mid+1,len(nums)-1)
        return search2(nums[mid+1:len(nums)-1],target)
    elif nums[mid] > target:
        # print("小于")
        # print("[low:high]",0,mid-1)
        return search2(nums[0:mid-1],target)
# search(nums,target)


#非递归版本 
def search3(nums,target):
    low = 0
    high = len(nums) - 1
    while(low<high):
        #(high - low) // 2 + low  防止溢出
        mid = (low +  high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1 
        elif nums[mid] == target:
            return  mid
    return -1

search3(nums,target)

