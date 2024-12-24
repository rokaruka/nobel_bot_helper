from aiogram.filters import CommandStart, Command
from aiogram.types import Message,CallbackQuery
from aiogram import  Router, F
import app.keyboard as kb
from app.keyboard import inline_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f' Привет! {message.from_user.first_name} \n Добро пожаловать в гастробар Nobel '
                            f'\n Подпишись на наш тг канал https://t.me/NobelExclusive '
                            f'\n Что бы быть в курсе всех событий ',
                        reply_markup=kb.main)



@router.callback_query(F.data == 'menu')
async def start (callback:CallbackQuery):
    await callback.message.answer('Мы больше, чем просто бар или ресторан.\n Мы создаем пространство, где каждый может быть самим собой - настоящим, без необходимости соответствовать ожиданиям общества и социальным ролям. \n '
                                  ' Мы создаем атмосферу, где каждый гость может расслабиться, отдохнуть, получить удовольствие и почувствовать себя по-настоящему уютно и комфортно.',reply_markup= await kb.inline_menu())


@router.callback_query(F.data == 'menu_Бар')
async def menu (callback:CallbackQuery):
    await callback.message.edit_text('Бар',reply_markup= await kb.bar_menu())

@router.callback_query(F.data == 'menu_Кухня')
async def menu (callback:CallbackQuery):
    await callback.message.edit_text('Кухня',reply_markup= await kb.kitchen_menu())

@router.callback_query(F.data == 'bar_item_Назад')
async def menu (callback:CallbackQuery):
    await callback.message.edit_text('Меню', reply_markup= await kb.inline_menu())

@router.callback_query(F.data == 'kitchen_item_Назад')
async def menu (callback:CallbackQuery):
    await callback.message.edit_text('Меню',reply_markup= await kb.inline_menu())

