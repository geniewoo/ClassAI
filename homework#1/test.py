import algo;
print("""
choose algorithmType
1 : DFS
2 : BFS
3 : IDS
""")
openListSize = 0
algorithmType = int(input())
firstPuzzle = input()
beforePosition = 0;
if algorithmType == 1 :
    searchAlgorithm = algo.Dfs();
success, beforePosition, openList, visitList = searchAlgorithm.searchNext((firstPuzzle, 0), [], [firstPuzzle], -1);
if success :
    print('fin')
else :
    print(success, beforePosition, openList, visitList)

visit = 1
while 1 :
    visit += 1;
    if len(openList) == 0 :
        print('no answer')

    currentPuzzle = openList.pop()
    success, beforePosition, openList, visitList = searchAlgorithm.searchNext(currentPuzzle, openList, visitList, beforePosition)
    if openListSize < len(openList) :
        openListSize = len(openList)
    if success :
        print('fin', visit, openListSize)
        break
    if visit % 10000 == 0 :
        print(visit)
        print(openListSize, openList)
