#278题 第一个错误版本
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
'''
#题目要求：找到错误版本后的第一个版本
#大体思路：
1、确定算法 类二分
2、注意点：没有边界值，类似于猜数字,但函数不会提醒多了还是少了
          查到错误的版本后，索引+1
          程序拒绝顺序暴力匹配，设置1为false，但可以逆序暴力匹配，当n过大时，存在超时错误
          n个版本中构成列表形状为 [false,...,false,true,...,true]
          位置锁定 且 二者bool不同
          位置锁定？  当b为0，a不是下一个mid，如何计算[c,a]区间的代码
          不是自己想的，根据错误信息，修正判断->原本应该是自动判断，而不是二次相等直接弹出
'''

class Solution(object):
    def firstBadVersion(self, n):
        j,low = 0,1
        i = None
        high = n
        while(n!=0):
            mid = (high - low) // 2 + low  
            if isBadVersion(mid):
                # print("ture:",mid)
                if ((abs(mid-j)==1) and ~bool(i)) :
                    return mid 
                if mid-j == 0:
                    return mid+1
                high = mid - 1  
                i = 1
                j = mid
            elif ~isBadVersion(mid):
                # print("false:",mid)
                if ((abs(mid-j)==1) and bool(i)):
                    return mid + 1
                if mid-j == 0:
                    return mid+1
                low = mid + 1
                i = 0
                j = mid
        return -1
        