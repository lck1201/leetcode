class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        Actually it's a DFS + DPTable Solution, Top-Down DP
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= 0:
            return True
        # if 1+2+3+....+maxChoosableInteger < desiredTotal, then no player can ever acquire desiredTotal, returning False
        if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
            return False
        self.memo = {}
        return self.win(list(range(1, maxChoosableInteger + 1)), desiredTotal)


    def win(self, nums, desiredTotal):
        """
        :param num:              available number pool
        :param desiredTotal:  desired total for victory
        """
        state = ''.join([str(i) for i in nums])
        # this is memoization, if this subproblem has already been calculated then return directly
        if state in self.memo:
            return self.memo[state]
        # this is the base case of the problem. if it is my turn and the max number in the array is enough to reach the desiredTotal , then i can force a win by simply picking this max number
        if nums[-1] >= desiredTotal:
            return True
        # pick a number, if the opponent can't force a win with the rest, that means i can force a win with picking this number
        for i in range(len(nums)):
            # pick each number in the number pool, and see using that if we attain desired Total
            if not self.win(list(nums[:i]) + list(nums[i + 1:]), desiredTotal - nums[i]): # opponent's turn, if he cannot win
                self.memo[state] = True
                return True
        # if there is no number that i can pick to force a win, then this array, total combination is false.
        self.memo[state] = False
        return False


Solution().canIWin(5,10)