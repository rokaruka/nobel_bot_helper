from aiogram.filters import CommandStart, Command
from aiogram.types import Message,CallbackQuery
from aiogram import  Router, F
import app.keyboard as kb
from app.keyboard import inline_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет \n Твой ID: {message.from_user.id},\n Твое имя: {message.from_user.first_name}',
                        reply_markup=kb.main)



@router.callback_query(F.data == 'menu')
async def start (callback:CallbackQuery):
    await callback.message.edit_text('hello',reply_markup= await kb.inline_menu())


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

