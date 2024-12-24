from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text ='Меню',callback_data='menu')],
    [InlineKeyboardButton(text='Контакты', callback_data= 'contacts'),InlineKeyboardButton(text='Nobel',url='https://www.nobel.bar/')],
],)


inline_kb = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text= 'Nobel',
                          url= 'https://www.nobel.bar/ ')]
])


menu = ['Бар','Кухня','Кальян','Главная']

kitchen_item =['Салаты','Горячее','Закуски','Назад']

bar_item = ['Коктейли','Вина','Крепкий алкоголь','Б\а напитки','Чай','Назад']

async def inline_menu ():
    keyboard = InlineKeyboardBuilder()
    for item in menu:
        keyboard.add(InlineKeyboardButton(text = item ,callback_data=f'menu_{item}'))
    return keyboard.adjust(2).as_markup()



async def bar_menu ():
    keyboard = InlineKeyboardBuilder()
    for  item in bar_item:
        keyboard.add(InlineKeyboardButton(text= item ,callback_data=f'bar_item_{item}'))
    return keyboard.adjust(2).as_markup()

async def kitchen_menu ():
    keyboard = InlineKeyboardBuilder()
    for item in kitchen_item:
        keyboard.add(InlineKeyboardButton(text= item ,callback_data=f'kitchen_item_{item}'))
    return keyboard.adjust(2).as_markup()