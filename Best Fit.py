def bestFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i] and (bestIdx == -1 or blockSize[bestIdx] > blockSize[j]):
                bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]

    print("Process no   Process size   Block no")
    for i in range(n):
        print(i + 1, "          ", processSize[i], end="        ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not allocated")

if _name_ == "_main_":
    bestFit([100, 200, 300, 400, 500], 5, [300, 100, 234, 100, 340], 5)