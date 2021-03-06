# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        else:
            return self.sym(root.left, root.right)
    def sym(self, left, right):
        if not left and not right: return True
        elif left and right :
            return left.val == right.val and \
            self.sym(left.left, right.right) and \
            self.sym(left.right, right.left)
        else:
            return False



