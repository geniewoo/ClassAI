import bisect

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


class Dfs:

    def searchNext(self, currentPuzzle, openList, visitList, beforePosition) :
        length = currentPuzzle[1];
        if currentPuzzle[0] == answer :
            return 1, [], [], [];

        index = currentPuzzle[0].index('0')

        for i in direct[index] :
            nextIndex =  i + index
            if 0 <= nextIndex and nextIndex < 9 :
                newNode = currentPuzzle[0]
                newNode = newNode[: index] + newNode[nextIndex] + newNode[index + 1 :]
                newNode = newNode[: nextIndex] + '0' + newNode[nextIndex + 1 :]

                isExist, insertIndex = binarySearch(visitList, newNode);
                if isExist == 0 :
                    openList.append((newNode, length + 1))
                    visitList.insert(insertIndex, newNode)

        return 0, index, openList, visitList


class Bfs:

    def searchNext(self, currentPuzzle, openList, visitList, beforePosition) :
        length = currentPuzzle[1];
        if currentPuzzle[0] == answer :
            return 1, [], [], [];

        index = currentPuzzle[0].index('0')

        for i in direct[index] :
            nextIndex =  i + index
            if 0 <= nextIndex and nextIndex < 9 :
                newNode = currentPuzzle[0]
                newNode = newNode[: index] + newNode[nextIndex] + newNode[index + 1 :]
                newNode = newNode[: nextIndex] + '0' + newNode[nextIndex + 1 :]

                isExist, insertIndex = binarySearch(visitList, newNode);
                if isExist == 0 :
                    openList.insert(0, (newNode, length + 1))
                    visitList.insert(insertIndex, newNode)

        return 0, index, openList, visitList

class Ids:

    def searchNext(self, currentPuzzle, openList, visitList, visitLengthList, beforePosition, maxLength) :
        length = currentPuzzle[1];

        if currentPuzzle[0] == answer :
            return 1, -1, [], [], [];
        index = currentPuzzle[0].index('0')
        if(length >= maxLength) :
            return 0, index, openList, visitList, visitLengthList

        for i in direct[index] :
            nextIndex =  i + index
            if 0 <= nextIndex and nextIndex < 9 :
                newNode = currentPuzzle[0]
                newNode = newNode[: index] + newNode[nextIndex] + newNode[index + 1 :]
                newNode = newNode[: nextIndex] + '0' + newNode[nextIndex + 1 :]

                isExist, insertIndex = binarySearch(visitList, newNode);
                if isExist == 0 :
                    openList.append((newNode, length + 1))
                    visitList.insert(insertIndex, newNode)
                    visitLengthList.insert(insertIndex, length + 1)
                elif length + 1 < visitLengthList[insertIndex] :
                    visitLengthList[insertIndex] = length + 1
                    openList.append((newNode, length + 1))

        return 0, index, openList, visitList, visitLengthList
