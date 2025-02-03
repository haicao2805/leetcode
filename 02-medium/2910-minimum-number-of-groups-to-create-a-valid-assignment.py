from typing import List, Dict


class Solution:
    def findSmallestAvailable(self, initial: int, mapping: Dict[int, int]) -> int:
        for i in range(initial, 0, -1):
            flag = True
            for seq in mapping.values():
                if seq % i > (seq - (seq % i)) // i:
                    flag = False
                    break
            if flag:
                return i
        return 1

    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        # Mapping ball -> sequences
        mapping = {}
        for ball in balls:
            current_seq = mapping.get(ball, 0)
            mapping[ball] = current_seq + 1

        # Find min seq
        min_seq = min(mapping.values())

        # Find smallest group that is available
        smallest = self.findSmallestAvailable(min_seq, mapping)

        # Group balls with this smallest
        res = 0
        for seq in mapping.values():
            mod = seq % (smallest + 1)
            res += (seq - mod) // (smallest + 1)

            if mod != 0:
                res += 1

        return res
