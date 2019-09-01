from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailMapToAccount = defaultdict(list)
        visited = [False] * len(accounts)
        ans = []

        for accIdx, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emailMapToAccount[email].append(accIdx)
        # DFS
        def dfs(accIdx, emails):
            if visited[accIdx]:
                return
            visited[accIdx] = True
            for j in range(1, len(accounts[accIdx])):
                email = accounts[accIdx][j]
                emails.add(email)
                for neighbor in emailMapToAccount[email]:
                    dfs(neighbor, emails)

        # main entry
        for accIdx, account in enumerate(accounts):
            if visited[accIdx]:
                continue
            name, emails = account[0], set()
            dfs(accIdx, emails)
            ans.append([name] + sorted(emails))

        return ans
