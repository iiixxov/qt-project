from dataclasses import dataclass
from typing import Optional

from sqlalchemy import BinaryExpression
from sqlalchemy.orm import Query

from app.core import Database


@dataclass
class QueryRequest:
    query: Query
    model: type[Database.Model]
    filter_: Optional[BinaryExpression]
