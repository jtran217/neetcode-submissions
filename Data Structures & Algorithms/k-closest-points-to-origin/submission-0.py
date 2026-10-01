class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        #[distance,x,y]

        for point in points:
            x,y = point

            distance =  math.sqrt((x - 0)**2 + (y-0)**2)
            heapq.heappush(minHeap,(distance,[x,y]))
        res = []
        for i in range(k):
            distance,point = heapq.heappop(minHeap)
            res.append(point)
        return res