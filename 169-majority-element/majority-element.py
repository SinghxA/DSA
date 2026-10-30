# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         count={}
#         for num in nums:
#             if num in count:
#                 count[num]+=1

#             else:
#                 count[num]=1

#         return max(count,key=count.get)

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         count = {}

#         for num in nums:
#             count[num] = count.get(num, 0) + 1

#         n = len(nums)

#         for key, value in count.items():
#             if value > n // 2:
#                 return key  

# # MOORE VOTING ALGO

# class Solution:
#     def majorityElement(self, nums: list[int]) -> int:
#         ele=nums[0]
#         count=0
#         for num in nums:
#             if num==ele:
#                 count+=1

#             else:
#                 count-=1
#                 if count==0:
#                     ele=num
#                     count=1

#         return ele

# or

class Solution:
    def majorityElement(self, nums: list[int]) -> int:            
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

                        

                    

            
            

       


