from collections.abc import Callable, Collection, Iterable
from typing import Any, ClassVar
from typing_extensions import Self

from django.core.checks.messages import CheckMessage
from django.core.exceptions import (
    MultipleObjectsReturned as BaseMultipleObjectsReturned,
)
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.models.manager import BaseManager
from django.db.models.options import Options
from django.db.models.query import QuerySet

class ModelStateFieldsCacheDescriptor: ...

class ModelState:
    db: str | None = ...
    adding: bool = ...
    fields_cache: ModelStateFieldsCacheDescriptor = ...

class ModelBase(type): ...

class Model(metaclass=ModelBase):
    DoesNotExist: ClassVar[type[ObjectDoesNotExist]]
    MultipleObjectsReturned: ClassVar[type[BaseMultipleObjectsReturned]]
    _meta: ClassVar[Options[Self]]
    _default_manager: ClassVar[BaseManager[Self]]
    objects: ClassVar[BaseManager[Self]]

    pk: Any = ...
    _state: ModelState
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @classmethod
    def add_to_class(cls, name: str, value: Any) -> Any: ...
    @classmethod
    def from_db(
        cls, db: str | None, field_names: Collection[str], values: Collection[Any]
    ) -> Self: ...
    def delete(
        self, using: Any = ..., keep_parents: bool = ...
    ) -> tuple[int, dict[str, int]]: ...
    async def adelete(
        self, using: Any = ..., keep_parents: bool = ...
    ) -> tuple[int, dict[str, int]]: ...
    def full_clean(
        self,
        exclude: Collection[str] | None = ...,
        validate_unique: bool = ...,
        validate_constraints: bool = ...,
    ) -> None: ...
    def clean(self) -> None: ...
    def clean_fields(self, exclude: Collection[str] | None = ...) -> None: ...
    def validate_unique(self, exclude: Collection[str] | None = ...) -> None: ...
    def validate_constraints(self, exclude: Collection[str] | None = ...) -> None: ...
    def unique_error_message(
        self,
        model_class: type[Self],
        unique_check: Collection[Callable[..., Any] | str],
    ) -> ValidationError: ...
    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None: ...
    async def asave(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> None: ...
    def save_base(
        self,
        raw: bool = ...,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: str | None = ...,
        update_fields: Iterable[str] | None = ...,
    ) -> Any: ...
    def refresh_from_db(
        self,
        using: str | None = ...,
        fields: list[str] | None = ...,
        from_queryset: QuerySet[Self] | None = ...,
    ) -> None: ...
    async def arefresh_from_db(
        self,
        using: str | None = ...,
        fields: list[str] | None = ...,
        from_queryset: QuerySet[Self] | None = ...,
    ) -> None: ...
    def get_deferred_fields(self) -> set[str]: ...
    @classmethod
    def check(cls, **kwargs: Any) -> list[CheckMessage]: ...
    def __getstate__(self) -> dict[Any, Any]: ...
