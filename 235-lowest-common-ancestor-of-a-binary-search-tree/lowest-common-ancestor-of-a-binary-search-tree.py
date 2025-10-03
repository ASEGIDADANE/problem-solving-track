# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        def lowestcommon(root,p,q):

            if not root:
                return
            if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
                return root
            if (root.val == q.val or root.val == p.val):
                return root
            if (root.val < p.val and root.val < q.val) or (root.val >  p.val and root.val > q.val):
                if( root.val < p.val and root.val < q.val):
                   root.right = lowestcommon(root.right, p, q)
                   return root.right
                else:
                    root.left = lowestcommon(root.left, p, q)
                    return root.left
        return lowestcommon(root, p, q)





        
        

        