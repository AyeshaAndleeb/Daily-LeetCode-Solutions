# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        # Agar tree empty hai to kuch nahi karna
        if root is None:
            return None

        # Left aur Right child ko swap kar do
        root.left, root.right = root.right, root.left

        # Recursively left subtree ko invert karo
        self.invertTree(root.left)

        # Recursively right subtree ko invert karo
        self.invertTree(root.right)

        # Root return kar do (inverted tree ka root)
        return root