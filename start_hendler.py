# Ипорт модулей aiogram
from aiogram.filters import Command
from aiogram import types, Router, F

# стороние модули
import asyncio

# Файлы



router = Router() # Создание роутера
users_list = set()


@router.message(Command('start'))
async def post(message: types.Message):
    await message.delete()
    global users_list
    chat_id = message.chat.id
    
    if chat_id not in users_list:
        users_list.add(chat_id)
    
    # Приветствие   
    text = "Приветствую!"
    sent_message = await message.answer("</>")
    full_message = ""
    delay = 0.2 # Уменьшаем задержку для более плавного чтения
    for letter in text:
        full_message += letter
        await sent_message.edit_text(full_message + " \u200B")
        await asyncio.sleep(delay)
    await asyncio.sleep(2)
    #

    # Вывод текста
    start_list_1 = [] # Вывод для предложений
    for i in start_list_1:
        await sent_message.edit_text(i)
        await asyncio.sleep(3)

    # Отправка голосового
    # voice_path = "" # path вашего voice
    # voice = FSInputFile(voice_path)
    # await asyncio.sleep(2)
    # await message.answer_voice(voice=voice)

    # Удаление сообщений
    # for counter_message in range(message_1, message_2.message_id+1):
    #     await message.bot.delete_message(chat_id=message.chat.id, message_id=counter_message)
    #     await asyncio.sleep(0.7)
