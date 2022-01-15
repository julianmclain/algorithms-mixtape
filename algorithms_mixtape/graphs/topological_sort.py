from typing import Dict, Optional, List


def topo_sort(graph: Dict[int, int]) -> List[int]:
    """Find a topological sorting of a graph using the "straightforward" algorithm from Tim Roughgarden
    """
    def make_topo_sort(graph: Dict[int, int], curr_label: int):
        if not graph:
            return
        sink = find_sink_vertex(graph)
        result[curr_label] = sink
        delete_vertex(sink, graph)
        make_topo_sort(graph, curr_label-1)
    
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

    graph_copy = graph.copy()  # make a copy since this implementation destroys the input
    n = len(graph_copy)
    curr_label = n - 1
    result = [0] * n
    make_topo_sort(graph_copy, curr_label)
    return result


def dfs_topo_sort(graph: Dict[int, int]) -> Optional[List[int]]: 
    """
    """
    pass
