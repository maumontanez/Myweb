from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def single_source_shortest_path_length(G: Graph[_Node], source: _Node, cutoff: int | None = None): ...
@_dispatchable
def single_target_shortest_path_length(G: Graph[_Node], target: _Node, cutoff: int | None = None): ...
@_dispatchable
def all_pairs_shortest_path_length(G: Graph[_Node], cutoff: int | None = None) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def bidirectional_shortest_path(G: Graph[_Node], source: str, target: str): ...
@_dispatchable
def single_source_shortest_path(G: Graph[_Node], source: str, cutoff: int | None = None): ...
@_dispatchable
def single_target_shortest_path(G: Graph[_Node], target: str, cutoff: int | None = None): ...
@_dispatchable
def all_pairs_shortest_path(G: Graph[_Node], cutoff: int | None = None) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def predecessor(
    G: Graph[_Node], source: str, target: str | None = None, cutoff: int | None = None, return_seen: bool | None = None
): ...
