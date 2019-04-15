def solution(values, weights, maxSize):
    values  = [0] + values
    weights = [0] + weights
    dp = [[0] * (maxSize + 1) for _ in range(len(values))]
    for thing in range(1, len(values)):
        for w in range(maxSize + 1):
            if weights[thing] > w:
                dp[thing][w] = dp[thing - 1][w]  # current item weights > package capacity, cannot be put inside
            else:
                dp[thing][w] = max(dp[thing - 1][w],  # NO put current item
                                   dp[thing - 1][w - weights[thing]] + values[thing])  # put inside current item
    print(dp[-1][-1])
    for line in dp:
        print(line)

values  = [7, 12, 18, 22, 28]
weights = [1, 2, 3, 5, 7]
maxSize = 8

solution(values, weights, maxSize)
