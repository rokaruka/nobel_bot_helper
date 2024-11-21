from aiogram.filters import CommandStart, Command
from aiogram.types import Message,CallbackQuery
from aiogram import  Router, F
import app.keyboard as kb
from app.keyboard import inline_kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет \n Твой ID: {message.from_user.id},\n Твое имя: {message.from_user.first_name}',
                        reply_markup=kb.main)

@router.message(Command('start'))
async def cmd_cocktails(message: Message):
        await  message.reply('main',
                        reply_markup=kb.main)


@router.callback_query(F.data == 'start')
async def start (callback:CallbackQuery):




