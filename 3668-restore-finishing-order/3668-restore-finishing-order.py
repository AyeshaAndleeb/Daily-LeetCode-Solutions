class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends_set = set(friends)
        result = []

        for runner in order:
            if runner in friends_set:
                result.append(runner)

        return result
