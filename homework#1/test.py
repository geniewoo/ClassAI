import algo;
print("""
choose algorithmType
1 : DFS
2 : BFS
3 : IDS
""")
algorithmType = int(input())
currentPuzzle = input()
beforePosition = 0;
if algorithmType == 1 :
    searchAlgorithm = algo.Dfs();
beforePosition, visitMemory = searchAlgorithm.firstFind(currentPuzzle);
print(beforePosition, visitMemory);
