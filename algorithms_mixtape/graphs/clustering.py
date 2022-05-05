from typing import List, Dict, Tuple
from operator import itemgetter

from algorithms_mixtape.union_finds.union_find import IntUnionFind


def kclustering(graph: Dict[int, List[Tuple[int, int]]], k: int):
    """ compute the maximum spacing of a k-clustering

    Note: very similar to Kruskal's MST algorithm
    """
    if len(graph) < k:
        raise ValueError("k must be greater than or equal to the number of vertices")

    edges = []
    for from_vertex, neighbors in graph.items():
        for to_vertex, cost in neighbors:
            edges.append((from_vertex, to_vertex, cost))
    edges.sort(key=itemgetter(2), reverse=True)

    uf = IntUnionFind(sorted(list(graph.keys())))
    num_clusters = len(graph)
    while num_clusters > k:
        from_vertex, to_vertex, _ = edges.pop()
        if uf.find(from_vertex) != uf.find(to_vertex):
            uf.union(from_vertex, to_vertex)
            num_clusters -= 1

    # find the next edge crossing 2 clusters
    while uf.find(edges[-1][0]) == uf.find(edges[-1][1]):
        edges.pop()
    _, _, next_distance = edges[-1]

    return next_distance
