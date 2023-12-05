class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        min_ = 0

        for i in range(len(distance)):
            if start < destination:
                cur_min = sum(distance[start:destination])
            else:
                cur_min = sum(distance[destination:start])
            min_ = min(cur_min,sum(distance)-cur_min)

        return min_