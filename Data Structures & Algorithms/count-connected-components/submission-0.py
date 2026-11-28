class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [ i for i in range(n) ]

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            
            if root_x == root_y:
                return False
            else:
                parent[root_y] = root_x
                return True
        
        count = n

        for x, y in edges:
            if union(x, y):
                count -= 1
        
        return count