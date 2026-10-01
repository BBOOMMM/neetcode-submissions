"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def dfs(self, node, visited):
        if node.val in visited:
            return visited[node.val]
        
        new_node = Node(val=node.val, neighbors=[])  # Node 还没创建呢
        visited[node.val] = new_node
        for adj_node in node.neighbors:
            new_node.neighbors.append( self.dfs(adj_node, visited) )

        return new_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        # 要用 visited 去记录是否需要创建新节点
        visited = {}
        return self.dfs(node, visited)
