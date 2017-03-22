import heuristicAlgo;
print("""
choose algorithmType
1 : A*
2 : IDA*
""")
algorithmType = int(input())
print("""
choose heuristic
1 : H1
2 : H2
""")
heuristicType = int(input())
print("input puzzle")
firstPuzzle = input()

if algorithmType == 1 :
    searchAlgorithm = heuristicAlgo.AStar;
else :
    searchAlgorithm = heuristicAlgo.IDAStar;

if heuristicType == 1 :
    heuristicMethod = heuristicAlgo.H1;
else :
    heuristicMethod = heuristicAlgo.H2;

openListSize = 0
visit = 0

if algorithmType == 1 :
    openList = [(firstPuzzle, 0, 0, 0)]
    totalCostList = [0]
    visitList = [firstPuzzle]
    visitLengthList = [0]
    beforePosition = -1
    while 1 :
        if len(openList) == 0 :
            print('no answer', visit, openListSize, len(visitList))
            break;

        currentPuzzle = openList.pop(0)
        totalCostList.pop(0)
        visit += 1
        success, openList, totalCostList, visitList, visitLengthList, beforePosition = searchAlgorithm.searchNext(currentPuzzle, openList, totalCostList, visitList, visitLengthList, beforePosition, heuristicMethod)
        if openListSize < len(openList) :
            openListSize = len(openList)
        if success :
            print('fin', visit, openListSize, currentPuzzle[0], currentPuzzle[1])
            break;
        if visit % 10000 == 0 :
            print(visit)
            print('openListSize : ',openListSize, len(visitList))
else :
    isFin = 0;
    maxLength = 1;
    while 1 :
        openList = [(firstPuzzle, 0, 0, 0)]
        totalCostList = [0]
        visitList = [firstPuzzle]
        visitLengthList = [0]
        beforePosition = -1
        while 1 :
            if len(openList) == 0 :
                print('no answer', visit, openListSize, len(visitList))
                break;

            currentPuzzle = openList.pop(0)
            totalCostList.pop(0)
            visit += 1
            success, openList, totalCostList, visitList, visitLengthList, beforePosition = searchAlgorithm.searchNext(currentPuzzle, openList, totalCostList, visitList, visitLengthList, beforePosition, heuristicMethod, maxLength)
            if openListSize < len(openList) :
                openListSize = len(openList)
            if success :
                print('fin', visit, openListSize, currentPuzzle[0], currentPuzzle[1])
                isFin = 1;
                break;
            if visit % 10000 == 0 :
                print(visit)
                print('openListSize : ',openListSize, len(visitList), openList[0:10])

        if isFin == 1 :
            break;
        else :
            maxLength += 1;
            print(maxLength)
