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
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited


def recursive_dfs(graph: dict, start: str, visited=[]) -> list:
    """Recursively find all reachable vertices using DFS.

    Parameters
    ----------
    graph : dict
    start : str
    visited : list

    Return
    ------
    list
        The vertices reachable from 'start' in the order that they were seen.
    """
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            recursive_dfs(graph, neighbor, visited)
    return visited
