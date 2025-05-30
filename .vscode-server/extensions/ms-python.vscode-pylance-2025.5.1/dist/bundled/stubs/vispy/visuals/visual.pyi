# Copyright (c) Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

import weakref
from collections.abc import Sequence
from typing import Any

import numpy as np

from .. import gloo
from ..gloo.program import Program
from ..util import Frozen, logger
from ..util.event import EmitterGroup, Event
from .shaders import MultiProgram, StatementList
from .transforms import TransformSystem

class VisualShare:
    def __init__(self): ...

class BaseVisual(Frozen):
    def __init__(self, vshare: VisualShare | None = None): ...
    @property
    def transform(self): ...
    @transform.setter
    def transform(self, tr): ...
    @property
    def transforms(self): ...
    @transforms.setter
    def transforms(self, trs): ...
    def get_transform(self, map_from: str = "visual", map_to: str = "render"): ...
    @property
    def visible(self): ...
    @visible.setter
    def visible(self, v): ...
    def view(self): ...
    def draw(self): ...
    def attach(self, filt: Any, view: None | VisualView = None): ...
    def detach(self, filt: Any, view: None | VisualView = None): ...
    def bounds(self, axis: int, view: VisualView | None = None): ...
    def _compute_bounds(self, axis, view): ...
    def _bounds_changed(self): ...
    def update(self): ...
    def _transform_changed(self, event=None): ...

class BaseVisualView:
    def __init__(self, visual): ...
    @property
    def visual(self): ...
    def _prepare_draw(self, view=None): ...
    def _prepare_transforms(self, view): ...
    def _compute_bounds(self, axis, view): ...
    def __repr__(self): ...

class Visual(BaseVisual):
    def __init__(
        self,
        vcode: str = "",
        fcode: str = "",
        gcode: str | None = None,
        program: None | Program = None,
        vshare: VisualShare | None = None,
    ): ...
    def set_gl_state(self, preset: str | None = None, **kwargs): ...
    def update_gl_state(self, *args, **kwargs): ...
    def _compute_bounds(self, axis, view): ...
    def _prepare_draw(self, view=None): ...
    def _prepare_transforms(self, view): ...
    @property
    def shared_program(self): ...
    @property
    def view_program(self): ...
    @property
    def _draw_mode(self): ...
    @_draw_mode.setter
    def _draw_mode(self, m): ...
    @property
    def _index_buffer(self): ...
    @_index_buffer.setter
    def _index_buffer(self, buf): ...
    def draw(self): ...
    def _configure_gl_state(self): ...
    def _get_hook(self, shader, name): ...
    def attach(self, filt: Any, view: None | VisualView = None): ...
    def detach(self, filt: Any, view: None | VisualView = None): ...

class VisualView(BaseVisualView, Visual):
    def __init__(self, visual): ...

class CompoundVisual(BaseVisual):
    def __init__(self, subvisuals: Sequence[BaseVisual]): ...
    def add_subvisual(self, visual: Visual): ...
    def remove_subvisual(self, visual: Visual): ...
    def _subv_update(self, event): ...
    def _transform_changed(self, event=None): ...
    def draw(self): ...
    def _prepare_draw(self, view): ...
    def _prepare_transforms(self, view): ...
    def set_gl_state(self, preset: str | None = None, **kwargs): ...
    def update_gl_state(self, *args, **kwargs): ...
    def attach(self, filt: Any, view: None | VisualView = None): ...
    def detach(self, filt: Any, view: None | VisualView = None): ...
    def _compute_bounds(self, axis, view): ...

class CompoundVisualView(BaseVisualView, CompoundVisual):
    def __init__(self, visual): ...

class updating_property:
    def __init__(self, fget=None, fset=None, doc=None): ...
    def __get__(self, obj, objtype=None): ...
    def __set__(self, obj, value): ...
    def __delete__(self, obj): ...
    def setter(self, fset): ...
