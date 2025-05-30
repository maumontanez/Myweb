from _typeshed import Incomplete
from collections.abc import Iterable, Iterator, Sequence
from re import Pattern

from pyflakes.reporter import Reporter

__all__ = ["check", "checkPath", "checkRecursive", "iterSourceCode", "main"]

PYTHON_SHEBANG_REGEX: Pattern[bytes]

def check(codeString: str, filename: str, reporter: Reporter | None = None) -> int: ...
def checkPath(filename, reporter: Reporter | None = None) -> int: ...
def isPythonFile(filename) -> bool: ...
def iterSourceCode(paths: Iterable[Incomplete]) -> Iterator[Incomplete]: ...
def checkRecursive(paths: Iterable[Incomplete], reporter: Reporter) -> int: ...
def main(prog: str | None = None, args: Sequence[Incomplete] | None = None) -> None: ...
