# Can't generate with stubgen because `import pywintypes` must be called first.
# Otherwise you get the error: "KeyError: 'pywintypes'"
from _typeshed import Incomplete
from collections.abc import Sequence
from datetime import datetime
from typing import ClassVar, Final, NoReturn, SupportsInt, overload
from typing_extensions import Never, deprecated

import _win32typing

class error(Exception):
    winerror: int
    funcname: str
    strerror: str
    def __init__(self, winerror: int, funcname: str, strerror: str, /): ...

class com_error(Exception): ...

class HANDLEType:
    def __init__(self, *args: Never) -> NoReturn: ...
    @property
    def handle(self) -> int: ...
    def Close(self) -> None: ...
    def close(self) -> None: ...
    def Detach(self) -> None: ...
    def __int__(self) -> int: ...

class TimeType(datetime):  # aka: PyTime, PyDateTime
    __name__: ClassVar[str] = "datetime"
    Format = datetime.strftime

IIDType = _win32typing.PyIID

def DosDateTimeToTime(FatDate: int, FatTime: int, /) -> TimeType: ...
def UnicodeFromRaw(_str: str, /) -> str: ...
def IsTextUnicode(_str: str, flags, /) -> tuple[Incomplete, Incomplete]: ...
def OVERLAPPED() -> _win32typing.PyOVERLAPPED: ...
def IID(iidString: str, is_bytes: bool = ..., /) -> _win32typing.PyIID: ...
def Time(timeRepr: SupportsInt | Sequence[SupportsInt] | TimeType, /) -> TimeType: ...
def CreateGuid() -> _win32typing.PyIID: ...
def ACL(bufSize: int = ..., /) -> _win32typing.PyACL: ...
def SID(buffer, idAuthority, subAuthorities, bufSize=..., /) -> _win32typing.PySID: ...
def SECURITY_ATTRIBUTES() -> _win32typing.PySECURITY_ATTRIBUTES: ...
def SECURITY_DESCRIPTOR() -> _win32typing.PySECURITY_DESCRIPTOR: ...
def HANDLE() -> HANDLEType: ...
def HKEY() -> _win32typing.PyHKEY: ...
def WAVEFORMATEX() -> _win32typing.PyWAVEFORMATEX: ...
@overload
@deprecated("Support for passing two ints to create a 64-bit value is deprecated; pass a single int instead")
def TimeStamp(timestamp: tuple[int, int], /) -> TimeType: ...
@overload
def TimeStamp(timestamp: int, /) -> TimeType: ...

FALSE: Final = False
TRUE: Final = True
WAVE_FORMAT_PCM: int
