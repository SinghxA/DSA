class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1

            else:
                count[num]=1

        ans=sorted(count,key=count.get,reverse=True)[:1]

        k=ans[0]  
        return k      