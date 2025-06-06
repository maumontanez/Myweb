# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import logging
from weakref import WeakKeyDictionary

from ...gloo import Program
from ...gloo.preprocessor import preprocess
from ...util import logger
from ...util.event import EventEmitter
from .compiler import Compiler
from .function import MainFunction
from .variable import Variable

class ModularProgram(Program):
    def __init__(self, vcode="", fcode="", gcode=None): ...
    @property
    def vert(self): ...
    @vert.setter
    def vert(self, vcode): ...
    @property
    def frag(self): ...
    @frag.setter
    def frag(self, fcode): ...
    @property
    def geom(self): ...
    @geom.setter
    def geom(self, gcode): ...
    def _dep_changed(self, dep, code_changed=False, value_changed=False): ...
    def draw(self, *args, **kwargs): ...
    def build_if_needed(self): ...
    def _build(self): ...
    def update_variables(self): ...
