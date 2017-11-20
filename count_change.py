# def count_change(money, coins):
#     ways = [1] + [0] * money
#     for coin in coins:
#         for i in range(coin, money + 1):
#             ways[i] += ways[i - coin]
#             print(ways)
#     return ways[money]


# print(count_change(4, [1, 2]))


def count_change(money, coin_list):
    ways = [1] + [0] * money
    for coin in coin_list:
        for i in range(coin, money + 1):
            ways[i] += ways[i - coin]
    return ways[money]


print(count_change(4, [1, 2]))
