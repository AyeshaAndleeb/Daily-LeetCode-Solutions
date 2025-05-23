from collections import deque


class RecentCounter:

    def __init__(self):
        # Queue to store the timestamps of pings
        self.q = deque()

    def ping(self, t: int) -> int:
        # Add the current ping time to the queue
        self.q.append(t)

        # Remove pings that are older than t - 3000
        while self.q[0] < t - 3000:
            self.q.popleft()

        # Return the number of pings in the last 3000 ms
        return len(self.q)
