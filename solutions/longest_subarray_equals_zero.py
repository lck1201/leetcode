def solution(arr):
    dp = [0] * (len(arr) + 1)
    dp[0] = arr[0]

    len_longest_subarr = 0
    for i in range(len(dp)):
        dp[i] = dp[i - 1] + arr[i-1]

    for i in range(len(dp) - 1):
        for j in range(i + 1, len(dp)):
            if dp[j] - dp[i] == 0:
                len_longest_subarr = max(len_longest_subarr, j - i)

    return len_longest_subarr

arr = [3, 0, -1, -2, -3, 1, 1, 1, 2, 3, 1, -2, -1]
print(solution(arr))