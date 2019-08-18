import sys

if __name__ == "__main__":
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    m = int(line[1])

    line = sys.stdin.readline().strip().split()
    store = [int(i) for i in line]

    line = sys.stdin.readline().strip().split()
    price = [int(i) for i in line]

    onceEntireBuyMoney = sum(price)
    entireBuyNum = m // onceEntireBuyMoney

    minIce = min(store)
    ans = minIce + entireBuyNum

    buyNum = minIce + entireBuyNum + 1
    moneyNeed = 0

    while moneyNeed < m:
        moneyNeed = sum([max(buyNum - store[i], 0) * price[i] for i in range(n)])

        if moneyNeed < m:
            ans += 1
            buyNum += 1

    print(ans)
