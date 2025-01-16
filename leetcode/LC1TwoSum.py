class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n               
            if diff in prevMap:             #checks to see if compliment value (diff) exists in prevMap hashtable
                return [prevMap[diff], i]       #returns solution as two elements 
            prevMap[n] = i
        return