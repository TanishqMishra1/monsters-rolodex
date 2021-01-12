# Answer-1
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
    
        return inorder(root)[k - 1]



# Answer-2
class Solution:
     def searchBST(self, root: TreeNode, val: int) -> TreeNode:
         if root == None:
             return None
         elif root.val == val:
             return root
         elif root.val>val:
              return self.searchBST(root.left,val)
         else:
              return self.searchBST(root.left,val)