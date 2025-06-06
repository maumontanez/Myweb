import logging
import re
from collections import OrderedDict

import numpy as np
from numpy.typing import ArrayLike

from ...util import logger
from ...util.eq import eq
from . import parsing
from .expression import FunctionCall, TextExpression
from .shader_object import ShaderObject
from .variable import Variable, Varying

# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

class Function(ShaderObject):
    def __init__(self, code, dependencies=None): ...
    def __setitem__(self, key, val): ...
    def __getitem__(self, key): ...
    def __call__(self, *args): ...
    def __contains__(self, key): ...

    # Public API methods

    @property
    def signature(self): ...
    @property
    def name(self): ...
    @property
    def args(self): ...
    @property
    def rtype(self): ...
    @property
    def code(self): ...
    @code.setter
    def code(self, code): ...
    @property
    def template_vars(self): ...
    def static_names(self): ...
    def replace(self, str1: str, str2: str): ...

    # Private methods

    def _parse_template_vars(self): ...
    def _get_replaced_code(self, names, version, shader): ...
    def definition(self, names, version, shader): ...
    def expression(self, names): ...
    def _clean_code(self, code): ...
    def __repr__(self): ...

class MainFunction(Function):
    def __init__(self, shader_type, *args, **kwargs): ...
    @property
    def signature(self): ...
    @property
    def version_pragma(self): ...
    def definition(self, obj_names, version, shader): ...
    def static_names(self): ...
    def add_chain(self, var): ...
    def add_callback(self, hook, func): ...
    def remove_callback(self, hook, func): ...

class FunctionChain(Function):
    def __init__(self, name: str | None = None, funcs: ArrayLike = ...): ...
    @property
    def functions(self): ...
    @functions.setter
    def functions(self, funcs): ...
    @property
    def signature(self): ...
    def _update(self): ...
    @property
    def code(self): ...
    @code.setter
    def code(self, c): ...
    @property
    def template_vars(self): ...
    def append(self, function, update=True): ...
    def __setitem__(self, index, func): ...
    def __getitem__(self, k): ...
    def insert(self, index, function, update=True): ...
    def remove(self, function, update=True): ...
    def definition(self, obj_names, version, shader): ...
    def static_names(self): ...
    def __repr__(self): ...

class StatementList(ShaderObject):
    def __init__(self): ...
    def add(self, item, position=5): ...
    def remove(self, item): ...
    def expression(self, obj_names): ...
