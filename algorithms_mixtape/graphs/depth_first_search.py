def dfs(graph: dict, start: str) -> set:
    """
    Find all reachable vertices using DFS
    :return: vertices reachable from 'start'
    """
    visited = set()
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for w in graph[v]:
                stack.append(w)
    return visited


def recursive_dfs(graph: dict, start: str, visited=set()) -> set:
    """Recursively find all reachable vertices using DFS.

    :return: The vertices reachable from 'start'
    """
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            recursive_dfs(graph, neighbor, visited)
    return visited
