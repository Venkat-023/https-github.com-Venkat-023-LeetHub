class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==0:
            return False
        def dfs(n):
            if n==1:
                return True
            if n%3!=0:
                return False
            return dfs(n/3)
        return dfs(n)