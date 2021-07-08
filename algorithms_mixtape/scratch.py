from typing import List, Set, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # initiate DFS from every node
        # When the call to DFS terminates, add 1 to island count if it visited at least 1 node
        def get_neighbors(row: int, column: int, grid: List[List[str]]):
            directions = [
                [1, 0],
                [-1, 0],
                [0, 1],
                [0, -1],
            ]
            neighbors = []
            for direction in directions:
                row_index = int(row) + direction[0]
                column_index = int(column) + direction[1]
                is_valid_row = 0 <= row_index < len(grid)
                is_valid_column = 0 <= column_index < len(grid[0])
                if is_valid_row and is_valid_column and grid[row_index][column_index] != "0":
                    neighbors.append((row_index, column_index))
            return neighbors

        def dfs(row: int, column: int, grid: List[List[str]], visited: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            if (row, column) not in visited:
                visited.add((row, column))
                for neighbor in get_neighbors(row, column, grid):
                    if neighbor not in visited:
                        neighbor_row, neighbor_column = neighbor
                        dfs(neighbor_row, neighbor_column, grid, visited)
            return visited

        if grid is None or len(grid) == 0:
            return 0

        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0
        visited = set()
        for r in range(nr):
            for c in range(nc):
                if (grid[r][c] == "1" and (r, c) not in visited):
                    num_islands += 1
                    visited.union(dfs(r, c, grid, visited))
        return num_islands



grid_one = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid_two = [
  ["1","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","1"]
]

x = Solution()
# print(x.numIslands(grid_one))
print(x.numIslands(grid_two))
