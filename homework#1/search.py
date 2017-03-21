import searchAlgo;
print("""
choose algorithmType
1 : DFS
2 : BFS
3 : IDS
""")
openListSize = 0
algorithmType = int(input())
print("input puzzle")
firstPuzzle = input()
beforePosition = 0;
if algorithmType == 1 :
    searchAlgorithm = searchAlgo.Dfs()
elif algorithmType == 2 :
    searchAlgorithm = searchAlgo.Bfs()
else :
    searchAlgorithm = searchAlgo.Ids()
visit = 1
if algorithmType != 3 :
    success, beforePosition, openList, visitList = searchAlgorithm.searchNext((firstPuzzle, 0), [], [firstPuzzle], -1);
    if success :
        print('fin')
    else :
        print(success, beforePosition, openList, visitList)

    while 1 :
        visit += 1
        if len(openList) == 0 :
            print('no answer', visit, openListSize, len(visitList))
            print(visitList[0:100])
            break;

        currentPuzzle = openList.pop()
        success, beforePosition, openList, visitList = searchAlgorithm.searchNext(currentPuzzle, openList, visitList, beforePosition)
        if openListSize < len(openList) :
            openListSize = len(openList)
        if success :
            print('fin', visit, openListSize, currentPuzzle[0], currentPuzzle[1])
            break
        if visit % 10000 == 0 :
            print(visit)
            print('openListSize : ',openListSize, len(visitList))
else :
    isFin = 0;
    maxLength = 1;
    while 1 :
        success, beforePosition, openList, visitList, visitLengthList = searchAlgorithm.searchNext((firstPuzzle, 0), [], [firstPuzzle], [0], -1, maxLength);
        if success :
            print('fin')
        else :
            print(success, beforePosition, openList, visitList)
        while 1 :
            visit += 1
            if len(openList) == 0 :
                print('no answer', visit, openListSize, len(visitList))
                break;

            currentPuzzle = openList.pop()
            success, beforePosition, openList, visitList, visitLengthList = searchAlgorithm.searchNext(currentPuzzle, openList, visitList, visitLengthList, beforePosition, maxLength)
            if openListSize < len(openList) :
                openListSize = len(openList)
            if success :
                print('fin', visit, openListSize, currentPuzzle[0], currentPuzzle[1])
                isFin = 1;
                break
            if visit % 10000 == 0 :
                print(visit)
                print('openListSize : ',openListSize, len(visitList))

        if isFin == 1 :
            break;
        else :
            maxLength += 1;
