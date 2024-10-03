# cach 1
def solve1():
    n = int(input("Nhap so luong phan tu: "))
    N = int(input("Nhap N: "))
    numbers = []
    for i in range(n):
        numbers.append(int(input(f"Nhap phan tu thu {i+1}: ")))

    # tao mang dp: voi dp[i] : so cach xep i phan tu bang gia tri N
    dp = [0] * (N + 1)

    # co 1 cach de xep N phan tu bang khong la khong chon phan tu nao
    dp[0] = 1

    for num in numbers:
        for i in range(num, N+1):
            dp[i] += dp[i-num]

    print(f"Voi N = {N} se co {dp[N]} to hop sap xep")


# cach 2
def solve2():
    result = []
    coins = []

    n = int(input("Nhap sl phan tu: "))
    N = int(input("Nhap N: "))

    coins = [int(input(f"Nhap phan tu thu {i+1}: ")) for i in range(n)]

    def mainSolve(idx_start, temp, sum):
        if sum == N:
            result.append(temp[:])

        if sum > N:
            return

        for i in range(idx_start, n):
            if sum + coins[i] <= N:
                temp.append(coins[i])
                mainSolve(i, temp, sum + coins[i])
                # lenh pop chay khi mainSolve return
                # -> gap phan tu khi them vao > N -> xoa
                temp.pop()

    mainSolve(0, [], 0)

    for num in result:
        print(num, end=" ")

    # tmp = [0] * (N+1)
    # sum = 0
    #  bd,i,sum : x[i] = a[j], j = bd -> n  try(0,0,0)

    # def mainSolve(idx_start, idx_main, sum):
    #     for i in range(idx_start, n, 1):
    #         if sum + coins[i] <= N:
    #             tmp[idx_main] = coins[i]
    #             if sum + coins[i] == N:
    #                 # sao chep mang tmp tu tmp[0] -> tmp[idx_main]
    #                 result.append(tmp[:idx_main+1])
    #             else:
    #                 mainSolve(idx_start, idx_main + 1, sum + coins[i])

    # mainSolve(0, 0, 0)

    # for i in range(len(result)):
    #     print(result[i], end=" ")


if __name__ == "__main__":
    solve2()
