# Tag: Math
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        chars = set(tasks)
        count = []
        for c in chars:
            count.append(tasks.count(c))
        count.sort()

        p = 0
        for i in range(len(count)):
            if count[i] == count[-1]:
                p += 1

        return max(len(tasks), (count[-1] - 1) * (n + 1) + p)