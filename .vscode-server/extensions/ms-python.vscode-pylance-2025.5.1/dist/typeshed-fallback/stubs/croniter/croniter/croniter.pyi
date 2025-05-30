import datetime
from _typeshed import Unused
from collections import OrderedDict
from collections.abc import Iterator
from re import Match, Pattern
from typing import Any, Final, Literal, overload
from typing_extensions import Never, Self, TypeAlias

_RetType: TypeAlias = type[float | datetime.datetime]
_Expressions: TypeAlias = list[str]  # fixed-length list of 5 or 6 strings

def is_32bit() -> bool: ...

OVERFLOW32B_MODE: Final[bool]

EPOCH: Final[datetime.datetime]
M_ALPHAS: Final[dict[str, int]]
DOW_ALPHAS: Final[dict[str, int]]
ALPHAS: Final[dict[str, int]]
step_search_re: Final[Pattern[str]]
only_int_re: Final[Pattern[str]]

WEEKDAYS: Final[str]
MONTHS: Final[str]
star_or_int_re: Final[Pattern[str]]
special_dow_re: Final[Pattern[str]]
re_star: Final[Pattern[str]]
hash_expression_re: Final[Pattern[str]]
MINUTE_FIELD: Final = 0
HOUR_FIELD: Final = 1
DAY_FIELD: Final = 2
MONTH_FIELD: Final = 3
DOW_FIELD: Final = 4
SECOND_FIELD: Final = 5
UNIX_CRON_LEN: Final = 5
YEAR_FIELD: Final = 6
SECOND_CRON_LEN: Final = 6
YEAR_CRON_LEN: Final = 7
SECOND_FIELDS: Final[tuple[int, int, int, int, int, int]]
UNIX_FIELDS: Final[tuple[int, int, int, int, int]]
YEAR_FIELDS: Final[tuple[int, int, int, int, int, int, int]]
CRON_FIELDS: Final[dict[str | int, tuple[int, ...]]]
VALID_LEN_EXPRESSION: Final[set[int]]
EXPRESSIONS: dict[tuple[str, bytes], _Expressions]

UTC_DT: Final[datetime.timezone]

def timedelta_to_seconds(td: datetime.timedelta) -> float: ...

class CroniterError(ValueError): ...
class CroniterBadTypeRangeError(TypeError): ...
class CroniterBadCronError(CroniterError): ...
class CroniterUnsupportedSyntaxError(CroniterBadCronError): ...
class CroniterBadDateError(CroniterError): ...
class CroniterNotAlphaError(CroniterError): ...

def datetime_to_timestamp(d: datetime.datetime) -> float: ...

class croniter(Iterator[Any]):
    MONTHS_IN_YEAR: Final = 12
    RANGES: Final[
        tuple[
            tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]
        ]
    ]
    DAYS: Final[
        tuple[
            Literal[31],
            Literal[28],
            Literal[31],
            Literal[30],
            Literal[31],
            Literal[30],
            Literal[31],
            Literal[31],
            Literal[30],
            Literal[31],
            Literal[30],
            Literal[31],
        ]
    ]
    ALPHACONV: Final[
        tuple[
            dict[Never, Never],
            dict[Never, Never],
            dict[str, str],
            dict[str, int],
            dict[str, int],
            dict[Never, Never],
            dict[Never, Never],
        ]
    ]
    LOWMAP: Final[
        tuple[
            dict[Never, Never],
            dict[Never, Never],
            dict[int, int],
            dict[int, int],
            dict[int, int],
            dict[Never, Never],
            dict[Never, Never],
        ]
    ]
    LEN_MEANS_ALL: Final[tuple[int, int, int, int, int, int, int]]
    bad_length: Final[str]

    tzinfo: datetime.tzinfo | None

    # Initialized to None, but immediately set to a float.
    start_time: float
    dst_start_time: float
    cur: float

    expanded: list[list[str]]
    nth_weekday_of_month: dict[str, set[int]]
    expressions: _Expressions

    def __init__(
        self,
        expr_format: str,
        start_time: float | datetime.datetime | None = None,
        ret_type: _RetType | None = ...,
        day_or: bool = True,
        max_years_between_matches: int | None = None,
        is_prev: bool = False,
        hash_id: str | bytes | None = None,
        implement_cron_bug: bool = False,
        second_at_beginning: bool | None = None,
        expand_from_start_time: bool = False,
    ) -> None: ...
    # Most return value depend on ret_type, which can be passed in both as a method argument and as
    # a constructor argument.
    def get_next(
        self, ret_type: _RetType | None = None, start_time: float | datetime.datetime | None = None, update_current: bool = True
    ) -> Any: ...
    def get_prev(
        self, ret_type: _RetType | None = None, start_time: float | datetime.datetime | None = None, update_current: bool = True
    ) -> Any: ...
    def get_current(self, ret_type: _RetType | None = None) -> Any: ...
    def set_current(self, start_time: float | datetime.datetime | None, force: bool = True) -> float: ...
    def __iter__(self) -> Self: ...
    def next(
        self,
        ret_type: _RetType | None = None,
        start_time: float | datetime.datetime | None = None,
        is_prev: bool | None = None,
        update_current: bool | None = None,
    ) -> Any: ...
    __next__ = next
    def all_next(
        self,
        ret_type: _RetType | None = None,
        start_time: float | datetime.datetime | None = None,
        update_current: bool | None = None,
    ) -> Iterator[Any]: ...
    def all_prev(
        self,
        ret_type: _RetType | None = None,
        start_time: float | datetime.datetime | None = None,
        update_current: bool | None = None,
    ) -> Iterator[Any]: ...
    def iter(self, ret_type: _RetType | None = ...) -> Iterator[Any]: ...
    def is_leap(self, year: int) -> bool: ...
    @classmethod
    def value_alias(
        cls,
        val: int,
        field: Literal[0, 1, 2, 3, 4, 5, 6],
        len_expressions: int | list[Any] | dict[Any, Any] | tuple[Any, ...] | set[Any] = 5,
    ) -> int: ...
    @classmethod
    def expand(
        cls,
        expr_format: str,
        hash_id: bytes | None = None,
        second_at_beginning: bool = False,
        from_timestamp: float | None = None,
    ) -> tuple[list[list[str]], dict[str, set[int]]]: ...
    @classmethod
    def is_valid(
        cls, expression: str, hash_id: bytes | None = None, encoding: str = "UTF-8", second_at_beginning: bool = False
    ) -> bool: ...
    @classmethod
    def match(
        cls,
        cron_expression: str,
        testdate: float | datetime.datetime | None,
        day_or: bool = True,
        second_at_beginning: bool = False,
    ) -> bool: ...
    @classmethod
    def match_range(
        cls,
        cron_expression: str,
        from_datetime: datetime.datetime,
        to_datetime: datetime.datetime,
        day_or: bool = True,
        second_at_beginning: bool = False,
    ) -> bool: ...

def croniter_range(
    start: float | datetime.datetime,
    stop: float | datetime.datetime,
    expr_format: str,
    ret_type: _RetType | None = None,
    day_or: bool = True,
    exclude_ends: bool = False,
    _croniter: type[croniter] | None = None,
    second_at_beginning: bool = False,
    expand_from_start_time: bool = False,
) -> Iterator[Any]: ...

class HashExpander:
    cron: croniter
    def __init__(self, cronit: croniter) -> None: ...
    @overload
    def do(
        self,
        idx: int,
        hash_type: Literal["r"],
        hash_id: None = None,
        range_end: int | None = None,
        range_begin: int | None = None,
    ) -> int: ...
    @overload
    def do(
        self, idx: int, hash_type: str, hash_id: bytes, range_end: int | None = None, range_begin: int | None = None
    ) -> int: ...
    @overload
    def do(
        self, idx: int, hash_type: str = "h", *, hash_id: bytes, range_end: int | None = None, range_begin: int | None = None
    ) -> int: ...
    def match(self, efl: Unused, idx: Unused, expr: str, hash_id: bytes | None = None, **kw: Unused) -> Match[str] | None: ...
    def expand(
        self,
        efl: object,
        idx: int,
        expr: str,
        hash_id: bytes | None = None,
        match: Match[str] | None | Literal[""] = "",
        **kw: object,
    ) -> str: ...

EXPANDERS: OrderedDict[str, HashExpander]
