import sys
from _typeshed import FileDescriptor
from collections.abc import Callable, Sequence
from types import TracebackType
from typing import Any
from typing_extensions import ParamSpec

from gevent._ffi.loop import _ErrorHandler
from gevent._types import _Callback
from gevent.libev import watcher

# this c extension is only available on posix
if sys.platform != "win32":
    _P = ParamSpec("_P")

    def get_version() -> str: ...
    def get_header_version() -> str: ...
    # the final item in the list could be an integer if one of the backends did not have a string mapping
    def embeddable_backends() -> list[str | int]: ...
    def recommended_backends() -> list[str | int]: ...
    def supported_backends() -> list[str | int]: ...
    def time() -> float: ...

    class loop:
        starting_timer_may_update_loop_time: bool
        error_handler: _ErrorHandler
        @property
        def approx_timer_resolution(self) -> float: ...  # readonly in Cython
        def __init__(self, flags: Sequence[str] | str | int | None = None, default: bool | None = None, ptr: int = 0) -> None: ...
        def destroy(self) -> None: ...
        @property
        def ptr(self) -> int: ...
        @property
        def WatcherType(self) -> type[watcher.watcher]: ...
        @property
        def MAXPRI(self) -> int: ...
        @property
        def MINPRI(self) -> int: ...
        def handle_error(
            self, context: object | None, type: type[BaseException] | None, value: BaseException | None, tb: TracebackType | None
        ) -> None: ...
        def run(self, nowait: bool = False, once: bool = False) -> None: ...
        def reinit(self) -> None: ...
        def ref(self) -> None: ...
        def unref(self) -> None: ...
        def break_(self, how: int = ...) -> None: ...
        def verify(self) -> None: ...
        def now(self) -> float: ...
        def update_now(self) -> None: ...
        update = update_now  # deprecated
        @property
        def default(self) -> bool: ...
        @property
        def iteration(self) -> int: ...
        @property
        def depth(self) -> int: ...
        @property
        def backend_int(self) -> int: ...
        @property
        def backend(self) -> str | int: ...
        @property
        def pendingcnt(self) -> int: ...
        def io(self, fd: FileDescriptor, events: int, ref: bool = True, priority: int | None = None) -> watcher.io: ...
        def closing_fd(self, fd: FileDescriptor) -> bool: ...
        def timer(self, after: float, repeat: float = 0.0, ref: bool = True, priority: int | None = None) -> watcher.timer: ...
        def signal(self, signum: int, ref: bool = True, priority: int | None = None) -> watcher.signal: ...
        def idle(self, ref: bool = True, priority: int | None = None) -> watcher.idle: ...
        def prepare(self, ref: bool = True, priority: int | None = None) -> watcher.prepare: ...
        def check(self, ref: bool = True, priority: int | None = None) -> watcher.check: ...
        def fork(self, ref: bool = True, priority: int | None = None) -> watcher.fork: ...
        def async_(self, ref: bool = True, priority: int | None = None) -> watcher.async_: ...
        def child(self, pid: int, trace: int = 0, ref: bool = True) -> watcher.child: ...
        def install_sigchld(self) -> None: ...
        def reset_sigchld(self) -> None: ...
        def stat(self, path: str, interval: float = 0.0, ref: bool = True, priority: bool | None = None) -> watcher.stat: ...
        # These technically don't allow the functions arguments to be passed in as kwargs
        # but there's no way to express that yet with ParamSpec, however, we would still like
        # to verify that the arguments match
        def run_callback(self, func: Callable[_P, Any], *args: _P.args, **_: _P.kwargs) -> _Callback: ...
        def run_callback_threadsafe(self, func: Callable[_P, Any], *args: _P.args, **_: _P.kwargs) -> _Callback: ...
        def fileno(self) -> FileDescriptor | None: ...
        @property
        def activecnt(self) -> int: ...
        @property
        def sig_pending(self) -> int: ...
        # the final item in the list could be a integer if some of the flags don't a string mapping
        @property
        def origflags(self) -> list[str | int]: ...
        @property
        def origflags_int(self) -> int: ...
        @property
        def sigfd(self) -> FileDescriptor: ...

    __all__ = [
        "get_version",
        "get_header_version",
        "supported_backends",
        "recommended_backends",
        "embeddable_backends",
        "time",
        "loop",
    ]
