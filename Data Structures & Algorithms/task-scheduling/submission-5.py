class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time =q[0][1]
            else:
                value = heapq.heappop(maxHeap) + 1
                if value:
                    q.append([value,time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        
        return time
