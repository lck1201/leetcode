class Solution:
    def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> bool:
        if len(pushed) != len(popped):
            return False

        ts = []
        while popped:
            val = popped[0]
            while (not ts or ts[-1] != val) and pushed:
                ts.append(pushed.pop(0))

            if ts[-1] != val:
                return False
            else:
                ts.pop(-1)
                popped.pop(0)

        return True


pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 2, 1]

re = Solution().validateStackSequences(pushed, popped)
print(re)
