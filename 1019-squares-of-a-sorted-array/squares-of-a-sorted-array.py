class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        neg=[]
        pos=[]

        # separate neg and pos

        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)


        # no neg numbers

        if len(neg) == 0:
            return [num*num for num in pos]



        # no pos number

        if len(pos)==0:
            res=[num*num for num in neg]
            res.reverse()
            return res

        # both exist

        pos=[num*num for num in pos]
        neg=[num*num for num in neg]
        neg.reverse()
        n=len(neg)
        p=len(pos)
        res=[]

        i=0
        j=0

        while i<n and j<p:
            if neg[i]>=pos[j]:
                res.append(pos[j])
                j+=1

            else:
                res.append(neg[i])
                i+=1

    # while loop khartam

        while i < n:
            res.append(neg[i])
            i += 1

        while j < p:
            res.append(pos[j])
            j += 1

        return res

            




            
        