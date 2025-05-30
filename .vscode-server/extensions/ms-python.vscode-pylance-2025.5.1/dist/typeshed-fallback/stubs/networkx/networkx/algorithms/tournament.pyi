from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def is_tournament(G: Graph[_Node]): ...
@_dispatchable
def hamiltonian_path(G: Graph[_Node]): ...
@_dispatchable
def random_tournament(n: int, seed: int | RandomState | None = None): ...
@_dispatchable
def score_sequence(G: Graph[_Node]): ...
@_dispatchable
def is_reachable(G: Graph[_Node], s: _Node, t: _Node): ...
@_dispatchable
def is_strongly_connected(G: Graph[_Node]): ...
