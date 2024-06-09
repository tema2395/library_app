from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from contextlib import asynccontextmanager


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    init_db(db)
    db.close()
    yield


app = FastAPI(lifespan=lifespan)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db(db: Session):
    genres = [
        "Трагедия",
        "Комедия",
        "История",
        "Мелодрама",
        "Роман",
        "Новелла",
        "Рассказ",
        "Документальная литература",
    ]
    for genre_name in genres:
        genre = crud.get_genre_by_name(db, genre_name)
        if not genre:
            genre = models.Genre(name=genre_name)
            db.add(genre)

    db.commit()


@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """Запрос на создание книги"""
    db_book = crud.create_book(db=db, book=book)
    return db_book


@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Запрос на чтение книг"""
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    """Запрос на чтение одной книги"""
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Запрос на удаление книги"""
    db_book = crud.delete_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.get("/genres/", response_model=list[schemas.Genre])
def read_genres(db: Session = Depends(get_db)):
    """Запрос на чтение жанров"""
    genres = crud.get_genres(db)
    return genres


@app.post("/genres/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    """Запрос на создание жанров"""
    db_genre = crud.create_genre(db=db, genre=genre)
    return db_genre


@app.get("/search/", response_model=list[schemas.Book])
def search_books(query: str, db: Session = Depends(get_db)):
    """Поиск книги по ключевому слову в названии или авторе"""
    books = (
        db.query(models.Book)
        .filter(
            (models.Book.title.contains(query)) | (models.Book.author.contains(query) | (models.Book.description.contains(query)))
        )
        .all()
    )
    return books


@app.get("/books/genres/{genre_id}", response_model=list[schemas.Genre])
def get_books_by_genre(genre_id: int, db: Session = Depends(get_db)):
    books = crud.get_books_by_genre(db, genre_id=genre_id)
    return books
