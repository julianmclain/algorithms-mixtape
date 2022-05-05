import random
from collections import defaultdict
from operator import itemgetter
from typing import Dict, List, Tuple, Set
from algorithms_mixtape.heaps.heap import Heap


def prim_mst_naive(graph: Dict[int, List[Tuple[int, int]]]) -> int:
    """
    Brute force search version of Prim's algorithm for computing the minimum cost spanning tree
    of an undirected and connected graph

    :return: minimum spanning tree cost
    """
    start = random.choice(list(graph.keys()))
    explored = {start}
    mst_cost = 0
    while len(explored) < len(graph):
        # Compute frontier crossing edges
        frontier_crossing_edges = []
        for vertex in explored:
            frontier_crossing_edges.extend([edge for edge in graph[vertex] if edge[0] not in explored])
        min_cost_edge = min(frontier_crossing_edges, key=lambda e: e[1])
        explored.add(min_cost_edge[0])
        mst_cost += min_cost_edge[1]

    return mst_cost


def prim_mst(graph: Dict[int, List[Tuple[int, int]]], heap: Heap) -> int:
    """
    Near linear time version of Prim's algorithm for computing  the minimum cost spanning tree
    of an undirected and connected graph

    :return: minimum spanning tree cost
    """
    start = random.choice(list(graph.keys()))
    explored = {start}
    mst_cost = 0
    for vertex, cost in graph[start]:
        heap.insert(cost, (start, vertex))

    while len(explored) < len(graph):
        min_edge_cost, (min_edge_tail, min_edge_head) = heap.extract_min()
        if min_edge_head not in explored:
            mst_cost += min_edge_cost
            explored.add(min_edge_head)
            # Add new frontier crossing edges to heap
            for vertex, cost in graph[min_edge_head]:
                if vertex not in explored:
                    heap.insert(cost, (min_edge_head, vertex))

    return mst_cost


def kruskal_mst_naive(graph: Dict[int, List[Tuple[int, int]]]) -> int:
    """
    Brute force search version of Kruskal's algorithm for computing the minimum cost spanning tree
    of an undirected and connected graph

    :return: minimum spanning tree cost
    """
    edges = []
    for from_vertex, neighbors in graph.items():
        for to_vertex, cost in neighbors:
            edges.append((from_vertex, to_vertex, cost))
    edges.sort(key=itemgetter(2))

    mst = defaultdict(list)
    for from_vertex, to_vertex, weight in edges:
        is_reachable = _is_reachable(mst, from_vertex, to_vertex)
        if not is_reachable:
            # since the graph is undirected, add both edges and later divide by 2 when computing min cost
            mst[from_vertex].append((to_vertex, weight))
            mst[to_vertex].append((from_vertex, weight))

    min_cost = sum(cost for edges in mst.values() for _, cost in edges) / 2
    return min_cost


def _is_reachable(graph: Dict[int, List[Tuple[int, int]]], start: int, target: int) -> bool:
    explored = set()
    _dfs(graph, start, target, explored)
    return target in explored


def _dfs(graph, start, target, explored) -> None:
    explored.add(start)
    for to_vertex, _ in graph[start]:
        if to_vertex not in explored:
            _dfs(graph, to_vertex, target, explored)
