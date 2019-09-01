from operator import itemgetter
class Solution:
    def canFinish(self, numCourses: int, prerequisites: 'List[List[int]]') -> 'bool':
        table = [{'pre_len': 0, 'post': []} for _ in range(numCourses)]

        for pair in prerequisites:
            pos, pre = pair
            table[pos]['pre_len'] += 1
            table[pre]['post'].append(pos)

        all_remove = set(range(numCourses))
        while all_remove:
            to_remove = set()
            for nc in all_remove:
                if table[nc]['pre_len'] == 0:
                    for ps in table[nc]['post']:
                        table[ps]['pre_len'] -= 1
                    to_remove.add(nc)
                    table[nc] = 0

            if not to_remove:
                return False

            all_remove -= to_remove

        return True


# visit node from child to parents
def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    visit = [0 for _ in range(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y) # to store course x's pre-requisites

    def notFormCouseLoop(i):
        '''
        travel node from child to parent,
        -1: being visited
        0: non-processed
        1: finished
        '''
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not notFormCouseLoop(j):
                return False
        visit[i] = 1
        return True

    for i in range(numCourses):
        if not notFormCouseLoop(i):
            return False

    return True