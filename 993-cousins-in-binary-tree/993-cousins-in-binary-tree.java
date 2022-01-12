class Pair{
    TreeNode parent;
    int depth;
    public Pair(TreeNode p, int d){
        this.parent = p;
        this.depth = d;
    }
}
class Solution {
    public Pair helper(TreeNode root, TreeNode parent, int target){
        if(root==null)
            return null;
        if(root.val==target)
            return new Pair(parent, 0);
        Pair left = helper(root.left, root, target);
        if(left!=null){
            left.depth++; // return depth+1 to the caller
            return left;
        }
        Pair right = helper(root.right, root, target);
        if(right!=null){
            right.depth++; // return depth+1 to the caller
            return right;
        }
        return null; // if target not found
        
    }
    public boolean isCousins(TreeNode root, int x, int y) {
        Pair x_ = helper(root, null, x); // O(N)
        Pair y_ = helper(root, null, y); // O(N)
        if(x_==null || y_==null) // if one or both target doesn't exists return false
            return false;
        return x_.depth==y_.depth && x_.parent!=y_.parent; // cousins are nodes with same depth with different immidiate parent
    }
}