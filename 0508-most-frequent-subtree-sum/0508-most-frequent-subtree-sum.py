# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 0
        hashmap=defaultdict(int)
        def dfs(root):
            if not root:
                return 0
            left,right=0,0
            left+=dfs(root.left)
            right+=dfs(root.right)
            total=left+right+root.val
            hashmap[total]+=1
            return root.val+left+right
        dfs(root)
        hashmap=sorted(hashmap.items(),key=lambda item:-item[1])
        res=[]
        freq=-1
        for k,v in hashmap:
            freq=max(freq,v)
            if v==freq:
                res.append(k)
            else:
                break
        return res