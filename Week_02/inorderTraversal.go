/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func inorderTraversal(root *TreeNode) []int {
    res:=[]int{}
    var traver func(root *TreeNode)
    traver=func(root *TreeNode){ 
        if root!=nil{
            traver(root.Left)
            res=append(res,root.Val)
            traver(root.Right)
        }
    }
    traver(root)
    return res
}
