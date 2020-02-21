from typing import List
import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append((target, float('inf')))
        tank = startFuel
        prev, ans = 0, 0

        for location, fuel in stations:
            tank -= (location - prev)
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -fuel)
            prev = location

        return ans

if __name__ == '__main__':

    s = Solution()
    target = 1000
    startFuel = 299
    stations = [[42,39],[132,236],[166,142],[434,7],[462,80],[518,103],[545,209],[656,104],[769,137],[811,67]]
    # target = 100
    # startFuel = 50
    # stations = [[25,50],[50,25]]
    print(s.minRefuelStops(target, startFuel, stations))