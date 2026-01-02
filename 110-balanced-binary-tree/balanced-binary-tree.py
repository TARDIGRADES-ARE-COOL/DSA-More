# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root: 
                return 0

            lefth = height(root.left)
            righth = height(root.right)

            if abs(lefth - righth)>1:
                balanced[0] = False
                return False

            return 1 + max(lefth, righth)

        height(root)
        return balanced[0]

        
    
            


        