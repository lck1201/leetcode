class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        if not amount:
            return amount
        MAX = amount + 1
        dp_table = [MAX] * (amount + 1)
        dp_table[0] = 1

        for i in range(1, amount + 1):
            mount = []
            for coin in coins:
                if coin <= i and dp_table[i - coin] > 0:
                    mount.append(dp_table[i - coin])
            if i in coins:
                mount.append(0)
            if not mount:
                continue
            dp_table[i] = min(mount) + 1

        if dp_table[amount] > 0:
            return dp_table[amount]
        else:
            return -1


print(Solution().coinChange([2, 5], 0))


# clear
class Solution2:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        if not amount:
            return amount

        MAX = float('inf')
        dp_table = [MAX] * (amount + 1)
        dp_table[0] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp_table[i] = min(dp_table[i], dp_table[i - coin] + 1)

        return dp_table[amount] if dp_table[amount] < MAX else -1
