from random import choice
from copy import deepcopy


def min_cut(graph):
    """Find the number of crossing edges in the minimum cut of a graph.

    This algorithm expects the graph to be represented as a dictionary that
    associates each vertex of the graph with a list of adjacent vertices. For
    example:

    graph = { '1': ['2', '3'],
              '2': ['1', '3'],
              '3': ['2', '4'],
              '4': ['3'],
              ...

    The representation is inspired by https://www.python.org/doc/essays/graphs/.

    Parameters
    ----------
    graph : dict

    Returns
    -------
    int
        The number of crossing edges in the minimum cut.
    """
    cuts = []
    for i in range(100):
        graph_copy = deepcopy(graph)
        cuts.append(_min_cut(graph_copy))
    return min(cuts)


def _min_cut(graph):
    while len(graph) > 2:
        endpoint_1 = choice(list(graph.keys()))
        endpoint_2 = choice(graph[endpoint_1])
        _contract_edge(graph, endpoint_1, endpoint_2)
    return len(graph[list(graph.keys())[0]])


def _contract_edge(graph, e1, e2):
    """Contract an edge of the graph.

    The contraction is performed by merging the 2 endpoints into a single super
    vertex. The first endpoint will be removed from the graph, and all of its
    neighbors will be reconnected to the second endpoint. Parallel references
    will be kept. Self-references will be removed.

    Parameters
    ----------
    graph: dict
        A dictionary representation of a graph
    e1: string
        The ID of the first endpoint
    e2: string
        The ID of the second endpoint
    """
    for vertex in graph[e1]:
        graph[vertex].remove(e1)
        if vertex == e1:
            raise Exception('There was a self-reference')
        if vertex != e2:
            graph[e2].append(vertex)
            graph[vertex].append(e2)
    del graph[e1]
