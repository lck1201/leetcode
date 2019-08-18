import sys

if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    k = int(line[1])

    line = sys.stdin.readline().strip().split()
    nums = [int(i) for i in line]

    ans = 0
    minLen = sum(nums[:k])
    tmp = sum(nums[:k])
    for i in range(k, n):
        tmp = tmp + nums[i] - nums[i - k]
        if tmp < minLen:
            ans = i - k + 1
            minLen = tmp

    print(ans + 1)
