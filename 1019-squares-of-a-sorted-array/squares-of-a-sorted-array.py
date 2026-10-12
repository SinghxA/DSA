class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        new  = []
        for i in range (len(nums)):
            new.append(nums[i]*nums[i])
 
        new.sort()

        return new

# Brute force 	
# Time	O(n log n)	
# Space	O(n)
        