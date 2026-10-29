class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        count={}
        for num in nums:
            if num in count:
                return True

            else:
                count[num]=1


        return False
        