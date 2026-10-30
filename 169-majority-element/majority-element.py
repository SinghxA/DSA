# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         count={}
#         for num in nums:
#             if num in count:
#                 count[num]+=1

#             else:
#                 count[num]=1

#         return max(count,key=count.get)

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        n = len(nums)

        for key, value in count.items():
            if value > n // 2:
                return key  