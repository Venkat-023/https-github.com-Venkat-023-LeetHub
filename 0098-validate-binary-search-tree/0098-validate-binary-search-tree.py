# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        list1=[]
        def preorder(root):
            if not root:
                return
            preorder(root.left)
            list1.append(root.val)
            preorder(root.right)
        preorder(root)
        for i in range(1,len(list1)):
            if list1[i-1]>=list1[i]:
                return False
                break
        return True
