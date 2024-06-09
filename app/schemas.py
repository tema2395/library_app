from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    description: str
    genre_id: int


class BookCreate(BookBase):
    genre_name: str | None = None


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        from_attributes = True
