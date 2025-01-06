from typing import List

class Solution:
    def getOperations(self, idx:int, ballPositions: List[int]):
        operations = 0
        for pos in ballPositions:
            operations += abs(pos - idx)
        return operations


    def minOperations(self, boxes: str) -> List[int]:
        idx = 0
        ballPositions: List[int] = []
        for box in boxes:
            if box == '1':
                ballPositions.append(idx)
            idx = idx + 1

        res: List[int] = [0] * len(boxes)
        for i in range(len(boxes)):
           res[i] = self.getOperations(i, ballPositions)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.minOperations("001011"))
    print(s.minOperations("110"))
