class Solution:
    def sortEvenOdd(self, nums):
        even = []
        odd = []

        # step 1: separate
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        # step 2: sort
        even.sort()
        odd.sort(reverse=True)

        # step 3: put back
        e = o = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even[e]
                e += 1
            else:
                nums[i] = odd[o]
                o += 1

        return nums
