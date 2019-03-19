# backtracking
def hasPath(matrix, string):
    if not matrix or not matrix[0]:
        return False

    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[0] * cols for _ in range(rows)]

    def has_path_core(matrix, nowString, row, col):
        if row >= 0 and row < rows and col >= 0 and col < cols and not visited[row][col]:
            nowString += matrix[row][col]  # does not change upper recursive level nowString
            if len(nowString) > len(string):
                return False
            if nowString == string:
                return True

            visited[row][col] = True
            hasP = has_path_core(matrix, nowString, row + 1, col) or \
                   has_path_core(matrix, nowString, row, col + 1) or \
                   has_path_core(matrix, nowString, row - 1, col) or \
                   has_path_core(matrix, nowString, row, col - 1)

            if not hasP:
                visited[row][col] = False
            else:
                return True
        return False

    for r in range(rows):
        for c in range(cols):
            if has_path_core(matrix, '', r, c):
                return True

    return False

matrix = [['a', 'b', 't', 'g'], ['c', 'f', 'c', 's'], ['j', 'd', 'e', 'h']]
print(hasPath(matrix, 'bfdop'))
