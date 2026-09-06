class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns=len(s)
        nt=len(t)
        cache={}
        def subs(i,j):
            if j==nt:
                return 1
            if i==ns:
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i]==t[j]:
                cache[(i,j)]=subs(i+1,j+1)+subs(i+1,j)
            else:
                cache[(i,j)]=subs(i+1,j)
            return cache[(i,j)]
        return subs(0,0)