# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(curr):
            if curr is None:
                return
            if curr.left is not None:
                traverse(curr.left)
            result.append(curr.val)
            if curr.right is not None:
                traverse(curr.right)
        
        traverse(root)

        return result 
