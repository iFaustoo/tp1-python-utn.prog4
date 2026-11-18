from fastapi import APIRouter, HTTPException, Query, status
from models.books import Book, BookUpdate

router = APIRouter()

libros: list[Book] = []


@router.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Book) -> Book:
    if any(existing_book.id == book.id for existing_book in libros):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un libro con ese id",
        )
    libros.append(book)
    return book


@router.get("/books")
def get_books(genre: str | None = Query(default=None)) -> list[Book]:
    if genre is None:
        return libros
    return [
        book for book in libros
        if book.genre.casefold() == genre.casefold()
    ]


@router.get("/books/{book_id}")
def get_book(book_id: int) -> Book:
    for book in libros:
        if book.id == book_id:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado",
    )


@router.put("/books/{book_id}")
def update_book(book_id: int, book_update: BookUpdate) -> Book:
    for index, book in enumerate(libros):
        if book.id == book_id:
            updated_book = Book(id=book_id, **book_update.model_dump())
            libros[index] = updated_book
            return updated_book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado",
    )


@router.delete("/books/{book_id}")
def delete_book(book_id: int) -> dict[str, str]:
    for book in libros:
        if book.id == book_id:
            libros.remove(book)
            return {"message": "Libro eliminado"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Libro no encontrado",
    )
