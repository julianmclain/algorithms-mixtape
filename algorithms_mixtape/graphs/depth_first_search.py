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
    s = [start]  # LIFO stack
    while s:
        v = s.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                s.append(w)
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


def topo_sort(graph: dict) -> list:
    # TODO
    # https://www.youtube.com/watch?v=AfSk24UTFS8
    # https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec14.pdf
    pass


def scc(graph: dict):
    """Compute the strongly connected components of a directed graph.

    Kosaraju's algorithm

    https://drive.google.com/file/d/1oyFlv810Ekc1QteXqDgb83vTkJEhAtnR/view
    """
    pass
