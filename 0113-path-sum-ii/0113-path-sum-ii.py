class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, current_path, remaining_sum):
            if not node:
                return

            current_path.append(node.val)
            remaining_sum -= node.val

            if not node.left and not node.right:
                if remaining_sum == 0:
                    result.append(list(current_path))

            dfs(node.left, current_path, remaining_sum)
            dfs(node.right, current_path, remaining_sum)

            current_path.pop()

        dfs(root, [], targetSum)
        return result
