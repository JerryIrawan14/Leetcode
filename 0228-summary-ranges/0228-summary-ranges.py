class Solution:
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges.append([n])
            else:
                ranges[-1][1:] = [n]
        return ['->'.join(map(str, r)) for r in ranges]
