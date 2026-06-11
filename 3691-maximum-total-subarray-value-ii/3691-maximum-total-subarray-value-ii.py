import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = n.bit_length()
        sp_max = [[0] * n for _ in range(LOG)]
        sp_min = [[0] * n for _ in range(LOG)]

        sp_max[0] = nums[:]
        sp_min[0] = nums[:]

        for j in range(1, LOG):
            for i in range(n - (1 << j) + 1):
                sp_max[j][i] = max(sp_max[j-1][i], sp_max[j-1][i + (1 << (j-1))])
                sp_min[j][i] = min(sp_min[j-1][i], sp_min[j-1][i + (1 << (j-1))])

        def query(l, r):
            length = r - l + 1
            p = length.bit_length() - 1
            hi = max(sp_max[p][l], sp_max[p][r - (1 << p) + 1])
            lo = min(sp_min[p][l], sp_min[p][r - (1 << p) + 1])
            return hi - lo

        heap = []
        for l in range(n):
            val = query(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        total = 0
        for _ in range(k):
            neg_val, l, r = heapq.heappop(heap)
            total += -neg_val
            if r > l:
                new_val = query(l, r - 1)
                heapq.heappush(heap, (-new_val, l, r - 1))

        return total