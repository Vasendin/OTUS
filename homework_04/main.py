"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from jsonplaceholder_requests import get_users, get_posts
from aiohttp import ClientSession
import config
from models import User, Base, Post

engine = create_async_engine(
    config.SQLA_ASYNC_CONN_URI,
    echo=config.SQLA_ECHO,
)


async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_schemas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(session: AsyncSession, users):
    for user in users:
        user = User(name=user['name'],
                    username=user['username'],
                    email=user['email']
                    )
        session.add(user)
    await session.commit()


async def create_posts(session: AsyncSession, posts):
    for post in posts:
        post = Post(user_id=post['userId'],
                    title=post['title'],
                    body=post['body']
                    )
        session.add(post)
    await session.commit()


async def async_main():
    # await create_schemas()
    users_data, posts_data = await asyncio.gather(
        get_users(),
        get_posts(),
    )
    async with async_session() as session:  # type: AsyncSession
        await create_users(session, users_data)
        await create_posts(session, posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
