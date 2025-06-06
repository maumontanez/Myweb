from typing import Any, Literal
from typing_extensions import Self

from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import Function, FunctionClass, UndefinedFunction
from sympy.core.kind import Kind
from sympy.core.numbers import Integer
from sympy.series.order import Order

class ExpBase(Function):
    unbranched = ...
    _singularities = ...
    @property
    def kind(self) -> Kind: ...
    def inverse(self, argindex=...) -> type[log]: ...
    def as_numer_denom(self) -> tuple[Any, Self] | tuple[Self, Any]: ...
    @property
    def exp(self) -> Basic: ...
    def as_base_exp(self) -> tuple[Self, Any | Order]: ...

class exp_polar(ExpBase):
    is_polar = ...
    is_comparable = ...
    def as_base_exp(self) -> tuple[Self, Any] | tuple[ExpBase, Any | Order]: ...

class ExpMeta(FunctionClass):
    def __instancecheck__(cls, instance) -> bool: ...

class exp(ExpBase, metaclass=ExpMeta):
    def fdiff(self, argindex=...) -> Self: ...
    @classmethod
    def eval(cls, arg): ...
    @property
    def base(self): ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...
    def as_real_imag(self, deep=..., **hints) -> tuple[Any, Any]: ...

def match_real_imag(expr) -> tuple[Any, Literal[0]] | tuple[Any, Any] | tuple[None, None]: ...

class log(Function):
    args: tuple[Expr]
    _singularities = ...
    def fdiff(self, argindex=...): ...
    def inverse(self, argindex=...) -> type[exp]: ...
    @classmethod
    def eval(cls, arg, base=...): ...
    def as_base_exp(self) -> tuple[Self, Any]: ...
    @staticmethod
    @cacheit
    def taylor_term(n, x, *previous_terms): ...
    def as_real_imag(
        self, deep=..., **hints
    ) -> (
        tuple[Self, Any]
        | tuple[Any, type[UndefinedFunction] | Any]
        | tuple[type[UndefinedFunction] | Any, type[UndefinedFunction] | Any]
    ): ...

class LambertW(Function):
    _singularities = ...
    @classmethod
    def eval(cls, x, k=...) -> Self | type[UndefinedFunction] | Integer | None: ...
    def fdiff(self, argindex=...): ...
