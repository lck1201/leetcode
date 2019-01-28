def dfs(word, row, col, board):
    if len(word) == 0:
        return True
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[0] != board[row][col]:
        return False

    tmp = board[row][col]  # First character is found, check the remaining part
    board[row][col] = '#'  # Avoid visit again
    # check whether can find "word" along one direction
    isExist = dfs(word[1:], row + 1, col, board) or \
              dfs(word[1:], row, col + 1, board) or \
              dfs(word[1:], row, col - 1, board) or \
              dfs(word[1:], row - 1, col, board)

    board[row][col] = tmp  # Maybe this path return False, however, must RECOVER BOARD for the other path to go through
    return isExist


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(word, row, col, board):
                    return True

        return False
