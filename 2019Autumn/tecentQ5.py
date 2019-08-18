import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n = int(line)

    chessMap = []
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        line = [int(i) for i in line]
        chessMap.append(line)

    table = [[(0, 1), (0, 1), (0, 1)] for _ in range(n)]
    table[0] = [(i, -1) if i == 0 else (i, 1) for i in chessMap[0]]
    ans = 0

    for r in range(1, n):
        n0, f0 = table[r - 1][0]
        n1, f1 = table[r - 1][1]
        n2, f2 = table[r - 1][2]

        for c in range(3):
            s0 = n0 + f0 * chessMap[r][c]
            s1 = n1 + f1 * chessMap[r][c]
            s2 = n2 + f2 * chessMap[r][c]
            if c == 0:
                if n0 + f0 * chessMap[r][c] > n1 + f1 * chessMap[r][c]:
                    tmp = (s0, f0 if chessMap[r][c] != 0 else -f0)
                else:
                    tmp = (s1, f1 if chessMap[r][c] != 0 else -f1)
                table[r][c] = tmp
            if c == 2:
                if n2 + f2 * chessMap[r][c] > n1 + f1 * chessMap[r][c]:
                    tmp = (s2, f2 if chessMap[r][c] != 0 else -f2)
                else:
                    tmp = (s1, f1 if chessMap[r][c] != 0 else -f1)
                table[r][c] = tmp
            if c == 1:
                # TODO: triple comparision
                if n2 + f2 * chessMap[r][c] > n1 + f1 * chessMap[r][c]:
                    tmp = (s2, f2 if chessMap[r][c] != 0 else -f2)
                else:
                    tmp = (s1, f1 if chessMap[r][c] != 0 else -f1)

                table[r][c] = tmp

    print(ans)
