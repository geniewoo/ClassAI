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
heuristicType = int(input))
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
