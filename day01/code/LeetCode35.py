'''
#搜索插入位置
题目需求 ：寻找值索引；若不在数值中，则按序插入数组；时间复杂度：O(logn)
难点：找不到，怎么插入？
插入当前mid前面还是后面 mid是最靠近target的，所以和mid比较时，选择合适位置
'''

#版本1  
# !错误，未考虑边界值
nums = [1,3,5,6] 
target = 2
def search(nums,target):
    low = 0
    high = len(nums) - 1
    while(low<=high):
        mid = (low +  high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1 
        elif nums[mid] == target:
            return  mid
    if nums[mid] > target:
        return mid-1
    else : return mid+1

a = search(nums,target)
print(a)


#版本2 
# 修正错误1
# ! 若mid和相邻元素都和target距离相等，存在错误
def search(nums,target):
        low = 0
        high = len(nums) - 1
        while(low<=high):
            mid = (low +  high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1 
            elif nums[mid] == target:
                return  mid
        if nums[mid] > target:
            return max(0,mid-1)
        else : return mid+1

#版本3
#修正错误2
#修正理由：若前插，表示代替mid原位，若后插，则mid+1 
#吸取经验，提笔前，理清插入顺序
class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        while(low<=high):
            mid = (low +  high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1 
            elif nums[mid] == target:
                return  mid
        if nums[mid] > target:
            return mid
        else : return mid+1