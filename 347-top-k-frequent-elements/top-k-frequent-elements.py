class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count={}
        ans=[0]*(k-1)
        for num in nums :
            if num in count:
                count[num]+=1
                
            else:
                count[num]=1

        ans = sorted(count,key=count.get,reverse=True)[:k]

        return ans



            

              

             

        