from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

@router.message(Command('start'))
async def greeting(msg: Message):
    await msg.answer(f'Hello, {msg.from_user.first_name}!')
