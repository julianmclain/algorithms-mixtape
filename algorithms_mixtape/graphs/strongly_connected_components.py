from typing import Dict, Tuple, List, Set, Iterable, Deque
from collections import defaultdict, deque


def scc(graph: Dict[str, Tuple[List[str], List[str]]]) -> Dict[str, int]:
    """Compute the size of all strongly connected components using Kosaraju's algorithm

    Recursive implementation kept running into max recursion depth on the large graph
    example, so it uses iterative DFS

    Parameters
    ----------
    graph : dict 
        Each value in graph dict is tuple of ([incoming edges], [outgoing edges])

    Return
    ------
    dict 
        dict of SCC label to SCC size 
    """
    topo_ordering = _dfs_topo_sort_iterative(graph)
    explored = set()
    scc_sizes = defaultdict(int)
    curr_scc = 0

    for vertex in topo_ordering:
        if vertex not in explored:
            _scc_dfs(graph, vertex, explored, scc_sizes, curr_scc)
            curr_scc += 1

    return scc_sizes


def _dfs_topo_sort_iterative(
    graph: Dict[str, Tuple[List[str], List[str]]]
) -> List[str]:
    """Find a topological sort of a graph using iterative depth-first search
    """

    def dfs(
        graph: Dict[str, Tuple[List[str], List[str]]],
        start: str,
        global_seen: Set[str],
        topo_order: List[str],
    ) -> List[str]:
        stack = [start]
        seen_this_search = []

        while stack:
            vertex = stack.pop()
            if vertex not in global_seen:
                global_seen.add(vertex)
                seen_this_search.append(vertex)
                for neighbor in graph[vertex][0]:
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


def _scc_dfs(
    graph: Dict[str, Tuple[List[str], List[str]]],
    start: str,
    seen: Set[str],
    scc_sizes: Dict[str, int],
    curr_scc: int,
) -> List[str]:
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in seen:
            seen.add(vertex)
            scc_sizes[curr_scc] = scc_sizes[curr_scc] + 1
            for neighbor in graph[vertex][1]:
                stack.append(neighbor)
