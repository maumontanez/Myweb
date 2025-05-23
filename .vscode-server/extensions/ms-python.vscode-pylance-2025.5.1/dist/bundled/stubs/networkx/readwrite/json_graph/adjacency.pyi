from collections.abc import Mapping
from itertools import chain

from ...classes.graph import Graph

__all__ = ["adjacency_data", "adjacency_graph"]

_attrs = ...

def adjacency_data(G: Graph, attrs: Mapping = ...) -> Mapping: ...
def adjacency_graph(data: Mapping, directed: bool = False, multigraph: bool = True, attrs: Mapping = ...): ...
