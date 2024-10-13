from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base
from datetime import date
from typing import Annotated


class Product(Base):
    id: Mapped[Annotated[int, mapped_column(primary_key=True)]]
    name: Mapped[str]
    price: Mapped[float]
    color: Mapped[str]
    size: Mapped[int]

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"name={self.name!r},")

    def __repr__(self):
        return str(self)
    
