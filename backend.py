from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

# Create the engine and session
engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class
Base = declarative_base()


# Define the association table for the many-to-many relationship
association_table = Table('association', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)


# Define the models
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")

    def __repr__(self):
        return f'<Author(id={self.id}, name="{self.name}")>'


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    categories = relationship("Category", secondary=association_table, back_populates="books")

    def __repr__(self):
        return f'<Book(id={self.id}, title="{self.title}", author_id={self.author_id})>'


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", secondary=association_table, back_populates="categories")

    def __repr__(self):
        return f'<Category(id={self.id}, name="{self.name}")>'


# Create the tables in the database
Base.metadata.create_all(engine)