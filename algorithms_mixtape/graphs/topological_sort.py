from typing import Dict, Optional, List, Set, Iterable, Deque
from collections import deque


def topo_sort(graph: Dict[int, int]) -> List[int]:
    """Find a topological sort of a graph using the "straightforward" algorithm from Tim Roughgarden
    """

    def do_topo_sort(graph: Dict[int, int], curr_label: int):
        if not graph:
            return
        sink = find_sink_vertex(graph)
        result[curr_label] = sink
        delete_vertex(sink, graph)
        do_topo_sort(graph, curr_label - 1)

    def find_sink_vertex(graph: Dict[int, int]) -> int:
        for v, neighbors in graph.items():
            if not neighbors:
                return v

        raise ValueError("No sink vertex found, the graph must contain a cycle")

    def delete_vertex(v: int, graph: Dict[int, int]) -> None:
        del graph[v]
        for edges in graph.values():
            if v in edges:
                edges.remove(v)

    if not graph:
        return []

    graph_copy = (
        graph.copy()
    )  # make a copy since this implementation destroys the input
    n = len(graph_copy)
    curr_label = n - 1
    result = [0] * n
    do_topo_sort(graph_copy, curr_label)
    return result


def dfs_topo_sort(graph: Dict[int, int]) -> List[int]:
    """Find a topological sort of a graph using recursive depth-first search

    Note: will hit Python max recursion depth with large graphs

    TODO: it would be fun to re-implement this lisp style without the for loop
    """
    n = len(graph)
    result = []

    def dfs(graph: Dict[int, int], start: int, seen: Set[int]):
        seen.add(start)
        for neighbor in graph[start]:
            if neighbor not in seen:
                dfs(graph, neighbor, seen)
        # Roughgarden recommends using a global var to track current position and assign
        # positions to vertices in reverse order (i.e. n to 0). In python that would've
        # required creating a class, so I just assigned in order seen and reversed it at
        # the end. Also could've used a linked list and prepended to the front
        result.append(start)

    seen = set()
    for v in graph:
        if v not in seen:
            dfs(graph, v, seen)

    result.reverse()
    return result


def dfs_topo_sort_iterative(graph: Dict[int, int]) -> List[int]:
    """Find a topological sort of a graph using iterative depth-first search
    """

    def dfs(
        graph: Dict[int, int], start: int, global_seen: Set[int], topo_order: List[int]
    ) -> List[int]:
        stack = [start]
        seen_this_search = []

        while stack:
            vertex = stack.pop()
            if vertex not in global_seen:
                global_seen.add(vertex)
                seen_this_search.append(vertex)
                for neighbor in graph[vertex]:
                    stack.append(neighbor)
        return seen_this_search

    def prepend(left: Iterable, right: Deque):
        for i in range(len(left) - 1, -1, -1):
            right.appendleft(left[i])

    topo_order = deque()
    seen = set()
    for vertex in graph:
        dfs_result = dfs(graph, vertex, seen, topo_order)
        prepend(dfs_result, topo_order)

    return topo_order
