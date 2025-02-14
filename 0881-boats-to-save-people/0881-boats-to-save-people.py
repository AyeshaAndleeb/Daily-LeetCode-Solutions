class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # ✅ Sort people by weight
        left, right = 0, len(people) - 1
        boats = 0

        while left <= right:  # ✅ Correct indentation
            if people[left] + people[right] <= limit:
                left += 1  # ✅ Pair the lightest person
            right -= 1  # ✅ Always take the heaviest person
            boats += 1  # ✅ Count this boat

        return boats
