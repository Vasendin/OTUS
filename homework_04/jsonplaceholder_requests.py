"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        response_json = await response.json()
        return response_json


async def get_users():
    async with ClientSession() as session:
        users = await fetch_json(session, USERS_DATA_URL)
        return users


async def get_posts():
    async with ClientSession() as session:
        posts = await fetch_json(session, POSTS_DATA_URL)
        return posts
