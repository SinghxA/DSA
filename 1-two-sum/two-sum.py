class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for i in range (len(nums)):
            dict[nums[i]]=i

        for i in range(len(nums)):
            need=target-nums[i]

            if need  in dict:
                if dict[need]!=i :
                   return dict[need],i

        