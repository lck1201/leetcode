class Solution:
    def findOrder(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        '''
        BFS
        '''
        table = [{'pre_len': 0, 'post': []} for _ in range(numCourses)]

        ans = list()
        for pair in prerequisites:
            post, pre = pair
            table[post]['pre_len'] += 1
            table[pre]['post'].append(post)

        all_remove = set(range(numCourses))
        while all_remove:
            to_remove = set()
            for course in all_remove:
                if table[course]['pre_len'] == 0:
                    for post_cource in table[course]['post']:
                        table[post_cource]['pre_len'] -= 1
                    ans.append(course)
                    to_remove.add(course)
                    table[course] = 0

            if not to_remove:
                return []

            all_remove -= to_remove

        return ans

    def findOrder2(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        '''
        DFS
        '''
        def dfs(table, i):
            nonlocal n, ans
            if table[i]['status'] == -1:
                return False
            if table[i]['status'] == 1:
                return True

            table[i]['status'] = -1
            for j in table[i]['pre']:
                if not self.dfs(table, j):
                    return False
            table[i]['status'] = 1

            ans[n] = i
            n += 1

            return True

        n = 0
        ans = [-1] * numCourses
        table = [{'status': 0, 'pre': []} for _ in range(numCourses)] #status 0: un-processed, -1: visiting, 1: visited

        for pair in prerequisites:
            post, pre = pair
            table[post]['pre'].append(pre)

        for i in range(numCourses):
            if not dfs(table, i):
                return list()

        return ans

