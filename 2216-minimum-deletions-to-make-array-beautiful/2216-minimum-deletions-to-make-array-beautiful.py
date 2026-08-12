class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack=[]
        rem=0
        for num in nums:
            idx=len(stack)-1
            if stack and idx%2==0 and stack[-1]==num:
                rem+=1
                continue
            stack.append(num)
        return rem if len(stack)%2==0 else rem+1