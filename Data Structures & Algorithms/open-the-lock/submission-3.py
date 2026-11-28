from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        locks = set(deadends)
        visited = {'0000'}

        queue = deque()
        queue.append('0000')

        adjs = {
            '0': ['1', '9'],
            '1': ['2', '0'],
            '2': ['3', '1'],
            '3': ['4', '2'],
            '4': ['5', '3'],
            '5': ['6', '4'],
            '6': ['7', '5'],
            '7': ['8', '6'],
            '8': ['9', '7'],
            '9': ['0', '8'],
        }

        res = []

        def nextwheel(s):
            for i in range(len(s)):
                for adj in adjs[s[i]]:
                    res.append( s[:i]+adj+s[i+1:] )
        
        count = 0
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                s = queue.popleft()
                if s == target:
                    return count
                res = []
                nextwheel(s)
                for re in res:
                    if re in visited or re in locks:
                        continue
                    visited.add(re)
                    queue.append(re)
            count += 1

        return -1
