from sqlalchemy.orm import Session
from . import models, schemas


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_books_by_genre(db: Session, genre_id: int):
    return db.query(models.Book).filter(models.Book.genre_id == genre_id).all()


def create_book(db: Session, book: schemas.BookCreate):
    if book.genre_name:
        genre = get_genre_by_name(db, book.genre_name)
        if not genre:
            genre = models.Genre(name=book.genre_name)
            db.add(genre)
            db.commit()
            db.refresh(genre)
        book.genre_id = genre.id

    db_book = models.Book(
        title=book.title,
        author=book.author,
        description=book.description,
        genre_id=book.genre_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book


def get_genres(db: Session):
    return db.query(models.Genre).all()


def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(**genre.model_dump())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def get_genre_by_name(db: Session, name: str):
    return db.query(models.Genre).filter(models.Genre.name == name).first()
