from collections import deque


def dfs(graph: dict, start: str) -> list:
    """Find all reachable vertices using DFS.

    Parameters
    ----------
    graph : dict
    start : str

    Return
    ------
    list
        The vertices reachable from 'start' in the order that they were seen.
    """
    visited = []
    s = deque([start])  # LIFO
    while s:
        v = s.popleft()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                s.appendleft(w)
    return visited

def topological_sort(graph: dict) -> list:
    pass

def strongly_connected_components():
    """
    Kosaraju's algorithm
    """
    pass

