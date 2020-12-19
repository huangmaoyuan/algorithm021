# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        hashmap= {v:i for i,v in enumerate(inorder)}
        def buildTreeHelper(preorder,p_start,p_end,inorder,i_start,i_end):
            if p_start==p_end:
                return None
            root=TreeNode(preorder[p_start])
            i_index=hashmap[root.val]
            LEFT=i_index-i_start
            root.left=buildTreeHelper(preorder,p_start+1,p_start+LEFT+1,inorder,i_start,i_index)
            root.right=buildTreeHelper(preorder,p_start+LEFT+1,p_end,inorder,i_index+1,i_end)
            return root
        return buildTreeHelper(preorder,0,len(preorder),inorder,0,len(inorder))
