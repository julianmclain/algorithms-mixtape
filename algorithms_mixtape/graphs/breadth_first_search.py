from collections import deque
import copy


def bfs(graph, start) -> list:
    """Find all reachable vertices using BFS.

    Parameters
    ----------
    graph : dict
    start : string

    Return
    ------
    list
        The list of reachable vertices in the order they were visited.
    """
    visited = [start]
    q = deque(start)  # FIFO
    while q:
        v = q.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                q.append(w)
    return visited


def shortest_path(graph: dict, start: str, end: str) -> int:
    """Find the shortest path to a vertex.

    Parameters
    ----------
    graph: dict
    start: str
    end: str

    Return
    ------
    int
        The fewest number of vertices in a path from start to end.
    """
    visited = [start]
    q = deque([(start, 0)])  # FIFO
    while q:
        v, dist = q.popleft()
        for w in graph[v]:
            if w == end:
                return dist + 1
            elif w not in visited:
                visited.append(w)
                q.append((w, dist + 1))
    raise ValueError(f"{end} is not reachable from {start}")


def shortest_path_remix(graph: dict, start: str, end: str) -> list:
    """Find the shortest path to a vertex.

    This algorithm makes a small change to the standard BFS procedure. Each
    'non-end' iteration of the while loop examines the edges of the current
    node and adds a copy of the entire path to the worklist. This way it keeps
    track of how it got to the current vertex.

    Parameters
    ----------
    graph: dict
    start: str
    end: str

    Return
    ------
    list
        An ordered list of vertices that represents the shortest path
        from start to end.
    """
    visited = [start]
    q = deque([[start]])
    while q:
        v = q.popleft()
        for w in graph[v[-1]]:
            if w == end:
                v.append(w)
                return v
            elif w not in visited:
                visited.append(w)
                path = copy.deepcopy(v)
                path.append(w)
                q.append(path)
    raise ValueError(f"{end} is not reachable from {start}")


def connected_components(graph):
    """Compute the number of connected components of an undirected graph.

    Parameters
    ----------
    graph: dict

    Return
    ------
    int
    """
    visited = []
    ccs = 0
    for v in graph:
        if v not in visited:
            connected_component = bfs(graph, v)
            visited.extend(connected_component)
            ccs += 1
    return ccs


def connected_components_remix(graph):
    """Compute the connected components of an undirected graph.

    Parameters
    ----------
    graph: dict

    Return
    ------
    list
        A list of the connected components of the graph.
    """
    visited = []
    ccs = []
    for v in graph:
        if v not in visited:
            connected_component = bfs(graph, v)
            visited.extend(connected_component)
            ccs.append(connected_component)
    return ccs
