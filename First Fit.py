def firstFit(blockSize, processSize):
    allocation = [-1] * len(processSize)
    for i, ps in enumerate(processSize):
        for j, bs in enumerate(blockSize):
            if bs >= ps:
                allocation[i] = j
                blockSize[j] -= ps
                break  # Exit the loop after allocating the block
    print("Process No. Process Size   Block no.")
    for i, ps in enumerate(processSize):
        print(i + 1, "           ", ps, end="           ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if _name_ == '_main_':
    firstFit([100, 500, 200, 300, 600], [212, 417, 112, 426])