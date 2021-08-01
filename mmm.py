#mean median and mode from an array of values
def mmm(list):
    length = len(list)
    mean = 0
    for i in range(length):
        mean += list[i]
    mean = mean / length

    median = []
    half = int(length/2)
    if length % 2 == 0:
        median.append(list[half - 1])
        median.append(list[half])
    else:
        median.append(list[half])

    mode = [] 
    max = 0

    for i in range(length):
        currentmax = 0

        for j in range(length):
            if list[i] == list[j]:
                currentmax += 1
        
        if currentmax > max and list[i] not in mode: ## if there is a new mode
            max = currentmax
            mode.clear()
            mode.append(list[i])
        if currentmax == max and list[i] not in mode: ## if there are multiple modes
            mode.append(list[i])


    meanmedianmode = ["mean: ",mean,"median: ", median,"mode: " ,mode]

    return meanmedianmode