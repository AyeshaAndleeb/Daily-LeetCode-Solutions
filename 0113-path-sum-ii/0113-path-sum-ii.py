class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, current_path, current_sum):
            if not node:
                return
            
            # current node ko path aur sum mein add karo
            current_path.append(node.val)
            current_sum += node.val
            
            # agar leaf node hai aur sum target ke barabar hai
            if not node.left and not node.right and current_sum == targetSum:
                result.append(current_path.copy())
            
            # left aur right subtree explore karo
            dfs(node.left, current_path, current_sum)
            dfs(node.right, current_path, current_sum)
            
            # wapis jaate waqt current node ko path se hata do
            current_path.pop()

        dfs(root, [], 0)
        return result