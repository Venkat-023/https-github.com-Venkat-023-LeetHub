class Solution:
    def minDeletions(self, s: str) -> int:
        hashmap=Counter(s)
        freq=list(hashmap.values())
        freq.sort(reverse=True)
        seen=set()
        res=0

        for i in range(len(freq)):
            while freq[i]!=0 and freq[i] in seen:
                freq[i]-=1
                res+=1
            seen.add(freq[i])
        return res
