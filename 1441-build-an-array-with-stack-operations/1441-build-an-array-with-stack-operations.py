class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        index = 0
        for num in range(1, n+1):
            if index == len(target):
                break

            result.append("Push")
            if num == target[index]:
                index += 1
            else:
                result.append("Pop")
        return result
        