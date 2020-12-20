/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func buildTree(preorder []int, inorder []int) *TreeNode {
    hashmap:=map[int]int{}
    for i,v :=range inorder{
        hashmap[v]=i
    }
    var buildTreeHelper func(perorder []int, p_start int, p_end int, inorder []int, i_start int, i_end int) *TreeNode
    buildTreeHelper = func(perorder []int, p_start int, p_end int, inorder []int, i_start int, i_end int) *TreeNode {
        if p_start==p_end{
            return nil
        }
        root_val:=preorder[p_start]
        root := &TreeNode{root_val, nil, nil}
        i_index:=hashmap[root_val]
        LEFT:=i_index-i_start
        root.Left=buildTreeHelper(preorder,p_start+1,p_start+LEFT+1,inorder,i_start,i_index)
        root.Right=buildTreeHelper(preorder,p_start+LEFT+1,p_end,inorder,i_index+1,i_end)
        return root
    }
    return buildTreeHelper(preorder,0,len(preorder),inorder,0,len(inorder))
}
