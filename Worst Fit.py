def worstFit(blockSize, m, processSize, n): 
    allocation = [-1] * n 
    for i in range(n): 
        worstIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i] and (worstIdx == -1 or blockSize[worstIdx] < blockSize[j]): 
                worstIdx = j 
        if worstIdx != -1: 
            allocation[i] = worstIdx 
            blockSize[worstIdx] -= processSize[i] 
    print("Process No. Process Size    Block no.") 
    for i in range(n): 
        print(i + 1, "           ", processSize[i], end = "           ") 
        if allocation[i] != -1: 
            print(allocation[i] + 1) 
        else: 
            print("Not Allocated") 

if _name_ == '_main_': 
    worstFit([100, 500, 200, 300, 600], 5, [212, 417, 112, 426], 4)