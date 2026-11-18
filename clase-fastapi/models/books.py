from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    publication_year: int


class BookUpdate(BaseModel):
    title: str
    author: str
    genre: str
    publication_year: int
