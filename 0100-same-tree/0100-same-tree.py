# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p, q):
        # Dono nodes None hain → trees same hain
        if not p and not q:
            return True

        # Agar ek None hai aur doosra nahi → same nahi hain
        if not p or not q:
            return False

        # Agar values different hain → same nahi
        if p.val != q.val:
            return False

        # Recursively left aur right subtrees compare karo
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)