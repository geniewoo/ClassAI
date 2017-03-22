direct = [(1, 3), (1, 3, -1), (3, -1), (-3, 1, 3), (-3, 1, 3, -1), (-3, 3, -1), (-3, 1), (-3, 1, -1), (-3, -1)];
answer = "123456780"

def binarySearch(searchList, searchStr) :
    first = 0
    last = len(searchList) - 1
    while 1 :
        if first > last :
            return 0, first
        half = (last - first) // 2 + first
        if searchList[half] == searchStr :
            return 1, half
        elif searchList[half] < searchStr :
            first = half + 1
        else :
            last = half - 1

class AStar:
    def searchNext(currentPuzzle, openList, totalCostList, visitList, visitLengthList, beforePosition, heuristicMethod) :
        length = currentPuzzle[1];
        if currentPuzzle[0] == answer :
            return 1, [], [], [], [], -1;
        index = currentPuzzle[0].index('0')

        for i in direct[index] :
            nextIndex = i + index
            if 0 <= nextIndex and nextIndex < 9 :
                newNode = currentPuzzle[0]
                newNode = newNode[: index] + newNode[nextIndex] + newNode[index + 1 :]
                newNode = newNode[: nextIndex] + '0' + newNode[nextIndex + 1 :]

                isExist, insertIndex = binarySearch(visitList, newNode);
                if isExist == 0 :
                    estimatedCost = heuristicMethod.estimateCost(newNode)
                    insertPriorityQueue(openList, (newNode, length + 1, estimatedCost, length + estimatedCost + 1), totalCostList)
                    visitList.insert(insertIndex, newNode)
                    visitLengthList.insert(insertIndex, length + 1)
                elif length + 1 < visitLengthList[insertIndex] :
                    estimatedCost = heuristicMethod.estimateCost(newNode)
                    visitLengthList[insertIndex] = length + 1
                    insertPriorityQueue(openList, (newNode, length + 1, estimatedCost, length + estimatedCost + 1), totalCostList)

        return 0, openList, totalCostList, visitList, visitLengthList, index

class IDAStar:
    def searchNext(currentPuzzle, openList, totalCostList, visitList, visitLengthList, beforePosition, heuristicMethod, maxLength) :
        length = currentPuzzle[1];
        if currentPuzzle[0] == answer :
            return 1, [], [], [], [], -1;
        index = currentPuzzle[0].index('0')

        if length > maxLength :
            return 0, openList, totalCostList, visitList, visitLengthList, index
        for i in direct[index] :
            nextIndex = i + index
            if 0 <= nextIndex and nextIndex < 9 :
                newNode = currentPuzzle[0]
                newNode = newNode[: index] + newNode[nextIndex] + newNode[index + 1 :]
                newNode = newNode[: nextIndex] + '0' + newNode[nextIndex + 1 :]

                isExist, insertIndex = binarySearch(visitList, newNode);
                if isExist == 0 :
                    estimatedCost = heuristicMethod.estimateCost(newNode)
                    if estimatedCost + 1 + length <= maxLength :
                        insertPriorityQueue(openList, (newNode, length + 1, estimatedCost, length + estimatedCost + 1), totalCostList)
                        visitList.insert(insertIndex, newNode)
                        visitLengthList.insert(insertIndex, length + 1)
                elif length + 1 < visitLengthList[insertIndex] :
                    estimatedCost = heuristicMethod.estimateCost(newNode)
                    if estimatedCost + 1 + length <= maxLength :
                        visitLengthList[insertIndex] = length + 1
                        insertPriorityQueue(openList, (newNode, length + 1, estimatedCost, length + estimatedCost + 1), totalCostList)

        return 0, openList, totalCostList, visitList, visitLengthList, index

class H1:
    def estimateCost(node) :
        count = 0
        for i in range(0, 8) :
            if i + 1 != int(node[i]) :
                count += 1
        return count

class H2:
    def estimateCost(node) :
        count = 0
        for i in range(0, 9) :
            if int(node[i]) != 0 :
                x1 = i // 3
                y1 = i % 3
                x2 = (int(node[i]) - 1) // 3
                y2 = (int(node[i]) - 1) % 3

                count += abs(x1 - x2)
                count += abs(y1 - y2)

        return count

def insertPriorityQueue(priorityQueue, insertData, totalCostList) :
    isExist, insertIndex = binarySearch(totalCostList, insertData[3])
    priorityQueue.insert(insertIndex, insertData)
    totalCostList.insert(insertIndex, insertData[3])
    return
