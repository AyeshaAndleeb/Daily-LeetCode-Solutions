class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        max_altitude = 0  # Start at 0

        for change in gain:
            altitude += change  # Update altitude
            max_altitude = max(max_altitude, altitude)  # Track highest altitude

        return max_altitude
