class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count=1
        i=0
        j=1
        while j< len(nums):
         
            # DUPL
            if nums[j]==nums[j-1]:
                j+=1
               
            # DIFF
            else:
                nums[i+1]=nums[j]
                i+=1
                count+=1
                j+=1

        return count


        