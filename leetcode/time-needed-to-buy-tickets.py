class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        queue = deque()
        hashmap = defaultdict(int)

        for i in range(len(tickets)):
            hashmap[i] = tickets[i]
            queue.append(i)

        while hashmap[k] > 0:
            peak = queue.popleft()

            hashmap[peak] -= 1
            if hashmap[peak]:
                queue.append(peak)

            total += 1

        return total