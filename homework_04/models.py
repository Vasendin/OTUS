"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, declared_attr
from sqlalchemy import Column, Text, Integer, ForeignKey, String

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

class Base:

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(bind=engine, cls=Base)
Session = sessionmaker(engine,
                       expire_on_commit=False,
                       class_=AsyncSession
                       )


class User(Base):
    username = Column(String(32), unique=True)
    name = Column(String(32), index=True)
    email = Column(String(32), index=True, unique=True)
    posts = relationship('Post', back_populates='user')

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            )


class Post(Base):
    title = Column(String(200),
                   nullable=False,
                   default="",
                   server_default=""
                   )
    body = Column(Text,
                  nullable=False,
                  default="",
                  server_default=""
                  )
    user_id = Column(Integer,
                     ForeignKey('blog_users.id'),
                     nullable=False,
                     unique=False,
                     index=True,
                     )
    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.id}, " \
               f"name={self.title!r}, " \
               f"author_id={self.user_id}"
