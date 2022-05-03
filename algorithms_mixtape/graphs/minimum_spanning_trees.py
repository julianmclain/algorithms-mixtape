import random
from typing import Dict, List, Tuple
from algorithms_mixtape.heaps.heap import Heap


def prim_mst_naive(graph: Dict[int, List[Tuple[int, int]]]) -> int:
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
