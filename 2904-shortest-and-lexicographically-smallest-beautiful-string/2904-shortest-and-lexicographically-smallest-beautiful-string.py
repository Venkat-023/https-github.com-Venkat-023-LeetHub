class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones,l=0,0
        n=len(s)
        t=n
        for r in range(n):
            if s[r]=='1':
                ones+=1
            if ones==k:
                t=min(t,r-l+1)
            while ones>=k:
                if s[l]=='1':
                    ones-=1
                l+=1
                if ones==k:
                    t=min(t,r-l+1)
        
        window,res=[],[]
        s=list(s)
        ones,l=0,0
        for r in range(n):
            if s[r]=='1':
                ones+=1
            window.append(s[r])
            if len(window)>t:
                if s[l]=='1':
                    ones-=1
                window.remove(s[l])
                l+=1
            if len(window)==t and ones==k:
                res.append(''.join(window[:]))
        res.sort()
        return res[0] if res else ''

        
        
