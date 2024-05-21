from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton("Посмотреть", url="https://i.ytimg.com/vi/QlChyW_6kYA/maxresdefault.jpg")
    but_inline_2 = InlineKeyboardButton("Что-то", url="https://patents.google.com/patent/US20090292143A1/en")
    keyboard_inline.add(but_inline, but_inline_2)
    return keyboard_inline