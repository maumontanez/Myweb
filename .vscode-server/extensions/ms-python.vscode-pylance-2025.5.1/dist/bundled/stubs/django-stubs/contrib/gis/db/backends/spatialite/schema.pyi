from typing import Any

from django.db.backends.sqlite3.schema import (
    DatabaseSchemaEditor as DatabaseSchemaEditor,
)

class SpatialiteSchemaEditor(DatabaseSchemaEditor):
    sql_add_geometry_column: str = ...
    sql_add_spatial_index: str = ...
    sql_drop_spatial_index: str = ...
    sql_recover_geometry_metadata: str = ...
    sql_remove_geometry_metadata: str = ...
    sql_discard_geometry_columns: str = ...
    sql_update_geometry_columns: str = ...
    geometry_tables: Any = ...
    geometry_sql: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def geo_quote_name(self, name: Any) -> Any: ...
    def column_sql(
        self, model: Any, field: Any, include_default: bool = ...
    ) -> Any: ...
    def remove_geometry_metadata(self, model: Any, field: Any) -> None: ...
    def create_model(self, model: Any) -> None: ...
    def delete_model(self, model: Any, **kwargs: Any) -> None: ...
    def add_field(self, model: Any, field: Any) -> None: ...
    def remove_field(self, model: Any, field: Any) -> None: ...
    def alter_db_table(
        self,
        model: Any,
        old_db_table: Any,
        new_db_table: Any,
        disable_constraints: bool = ...,
    ) -> None: ...
