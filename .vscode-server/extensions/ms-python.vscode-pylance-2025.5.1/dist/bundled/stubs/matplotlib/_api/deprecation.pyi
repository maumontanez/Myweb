import contextlib
from collections.abc import Iterator
from functools import partial
from typing import Callable

class MatplotlibDeprecationWarning(DeprecationWarning): ...

def warn_deprecated(
    since: str,
    *,
    message: str = ...,
    name: str = ...,
    alternative: str = ...,
    pending: bool = ...,
    obj_type: str = ...,
    addendum: str = ...,
    removal: str = ...,
) -> None: ...
def deprecated(
    since: str,
    *,
    message: str = ...,
    name: str = ...,
    alternative: str = ...,
    pending: bool = ...,
    obj_type: str = ...,
    addendum: str = ...,
    removal: str = ...,
) -> Callable: ...

class deprecate_privatize_attribute:
    def __init__(self, *args, **kwargs) -> None: ...
    def __set_name__(self, owner, name) -> None: ...

DECORATORS: dict = ...

def rename_parameter(since: str, old: str, new: str, func: None | Callable = ...) -> partial | Callable: ...

class _deprecated_parameter_class:
    def __repr__(self): ...

def delete_parameter(since: str, name: str, func: None | Callable = ..., **kwargs) -> partial | Callable: ...
def make_keyword_only(since: str, name: str, func: None | Callable = ...) -> partial | Callable: ...
def deprecate_method_override(method, obj, *, allow_empty: bool = ..., **kwargs): ...
@contextlib.contextmanager
def suppress_matplotlib_deprecation_warning() -> Iterator[None]: ...
