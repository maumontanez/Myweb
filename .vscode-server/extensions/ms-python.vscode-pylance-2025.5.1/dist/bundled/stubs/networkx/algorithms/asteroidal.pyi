from collections.abc import Mapping

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = ["is_at_free", "find_asteroidal_triple"]

def find_asteroidal_triple(G: Graph) -> list | None: ...
def is_at_free(G: Graph) -> bool: ...
def create_component_structure(G: Graph) -> Mapping: ...
