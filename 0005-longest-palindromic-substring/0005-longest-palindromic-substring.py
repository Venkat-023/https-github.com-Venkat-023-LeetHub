class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def check(i,j):
            while i>=0 and j<n and s[i]==s[j]:
                i-=1
                j+=1
            res=s[i+1:j]
            return res

        max_len=1
        res=s[0]
        for i in range(len(s)):
            even=check(i,i)
            odd=check(i,i+1)
            if len(odd)>max_len:
                max_len=len(odd)
                res=odd
            if len(even)>max_len:
                max_len=len(even)
                res=even
        return res