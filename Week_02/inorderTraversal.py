class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        
        def traver(root):
            if root:
                traver(root.left)
                res.append(root.val)
                traver(root.right)
        traver(root)
        
        return res
