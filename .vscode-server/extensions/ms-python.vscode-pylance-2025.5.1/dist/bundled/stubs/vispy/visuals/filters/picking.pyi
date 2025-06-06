# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import struct

from .base_filter import Filter

class PickingFilter(Filter):
    FRAG_SHADER: str = ...

    def __init__(self, id_=None): ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id): ...
    @property
    def enabled(self): ...
    @enabled.setter
    def enabled(self, e): ...
    @property
    def color(self): ...
