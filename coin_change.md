[5, 2, 1] 
target = 11

memo = {
    0: 0,
    1: 1,
    6: 2,
}

dfs(11)
return 3
minCoins = float('inf') <- update to 3
    coin 5
        dfs(6)
        return 2
        minCoins = float('inf') <- update to 2
            coin 5
                dfs(1)
                return 1
                minCoins = float('inf') <- update to 1
                    coin 5
                        ...ignore
                    coin 2
                        ...ignore
                    coin 1
                        dfs(0)
                        return 0 (amount in memo)
            coin 2
                ...
            coin 1
                ...
    coin 2  
    coin 1