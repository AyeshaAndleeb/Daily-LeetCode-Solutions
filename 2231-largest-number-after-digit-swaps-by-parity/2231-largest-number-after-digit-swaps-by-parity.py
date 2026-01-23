class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(str(num))   # 🔹 missing step

        odd = []
        even = []

        # step 1: separate digits
        for digit in digits:
            if int(digit) % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)

        # step 2: sort descending
        odd.sort(reverse=True)
        even.sort(reverse=True)

        res = []
        e = 0
        o = 0

        # step 3: rebuild number
        for d in digits:
            if int(d) % 2 == 0:
                res.append(even[e])  # ✅ use pointer
                e += 1
            else:
                res.append(odd[o])   # ✅ use pointer
                o += 1

        return int("".join(res))
