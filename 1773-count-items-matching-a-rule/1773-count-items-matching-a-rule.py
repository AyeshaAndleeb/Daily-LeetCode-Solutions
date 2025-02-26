class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        # Find the index to check
        index = {"type": 0, "color": 1, "name": 2}[ruleKey]

        # Count matching items
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count