from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text ='Меню',callback_data='menu')],
    [InlineKeyboardButton(text='Контакты', callback_data= 'contacts'),InlineKeyboardButton(text='Назад',callback_data='back')],
],)


inline_kb = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text= 'Nobel',
                          url= 'https://www.nobel.bar/ ')]
])


menu = ['Бар','Кухня','Кальян',]

async def inline_menu ():
    keyboard = InlineKeyboardBuilder()
    for item in menu:
        keyboard.add(InlineKeyboardButton(text= item ,callback_data=f'menu_{menu}'))
    return keyboard.adjust(2).as_markup()