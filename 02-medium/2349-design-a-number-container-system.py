from typing import List
import heapq


class NumberContainers:
    def __init__(self):
        self.numToIdx: dict[int, List[int]] = {}
        self.idxToNum: dict[int, int] = {}

    def change(self, index: int, number: int) -> None:
        self.idxToNum[index] = number
        if number not in self.numToIdx:
            self.numToIdx[number] = [index]
        else:
            heapq.heappush(self.numToIdx[number], index)

    def find(self, number: int) -> int:
        if number not in self.numToIdx:
            return -1
        while self.numToIdx[number]:
            idx = self.numToIdx[number][0]
            if self.idxToNum[idx] == number:
                return idx
            heapq.heappop(self.numToIdx[number])
        return -1


if __name__ == "__main__":
    s = NumberContainers()
    print(s.find(10))
