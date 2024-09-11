import asyncio
from main import bot
from aiogram.types import Message
from aiogram.utils.media_group import MediaGroupBuilder
from keyboards import ShareKeyboard, ShareText
import materials.starting as starting
import materials.day1 as day1
import materials.day2 as day2
import materials.day3 as day3
import materials.day4 as day4
import materials.day5 as day5
import materials.day6 as day6
import materials.day7 as day7
import materials.day8 as day8
import materials.day9 as day9
import materials.day10 as day10

VIDEO_AWAIT = 180
TEXT_AWAIT = 720
PHOTO_AWAIT = 900
QUESTION_AWAIT = 7200

async def send_starting(message : Message):
    await message.answer_video(
        video=starting.video1
    )
    await asyncio.sleep(60)
    await message.answer_photo(
        photo=starting.photo1
    )
    await message.answer_document(
        document=starting.pdf1
    )
    await message.answer(text=starting.caption1)
    group1 = MediaGroupBuilder()
    for f in [starting.pdf2, starting.pdf3, starting.pdf4]:
        group1.add_document(media=f)
    await message.answer_media_group(
        media=group1.build()
    )
    await message.answer(text=starting.text1, parse_mode='MarkdownV2')
    await message.answer(text=starting.text2, parse_mode='MarkdownV2')
    await asyncio.sleep(60)
    group2 = MediaGroupBuilder()
    for photo in [starting.photo2, starting.photo3]:
        group2.add_photo(media=photo)
    await message.answer_media_group(
        media=group2.build()
    )
    await message.answer_photo(photo=starting.photo4, caption=starting.caption2)
    await message.answer_photo(photo=starting.photo5, caption=starting.caption3)


async def message_day1(user_id: int):
    await bot.send_message(chat_id=user_id, text=day1.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day1.video1, caption="Лимон 🍋\n1 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day1.text1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day1.text2, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day1.photo1, caption="Пей Лимон - получишь миллион")
    await bot.send_photo(chat_id=user_id, photo=day1.photo2)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)


async def message_day2(user_id: int):
    await bot.send_message(chat_id=user_id, text=day2.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day2.video1, caption="Мята\n2 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day2.text1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day2.text2, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day2.text3, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day2.text4, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day2.text5, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day2.photo1)
    await bot.send_photo(chat_id=user_id, photo=day2.photo2)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day3(user_id: int):
    await bot.send_message(chat_id=user_id, text=day3.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day3.video1, caption="Лаванда\n3 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day3.text1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day3.text2, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day3.text3, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day3.text4, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day3.photo1)
    await bot.send_photo(chat_id=user_id, photo=day3.photo2)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day4(user_id: int):
    await bot.send_message(chat_id=user_id, text=day4.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day4.video1, caption="Чайное дерево 🍋\n4 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day4.text1)
    await bot.send_message(chat_id=user_id, text=day4.text2)
    await bot.send_message(chat_id=user_id, text=day4.text3)
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day4.photo1)
    await bot.send_photo(chat_id=user_id, photo=day4.photo2)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day5(user_id: int):
    await bot.send_message(chat_id=user_id, text=day5.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day5.video1, caption="Орегано\n5 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day5.text1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day5.text2, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day5.text3, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day5.text4, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    group1 = MediaGroupBuilder(
        caption="Пример использования эфирного масла орегано при подошвенных бородавках . Результат за две недели.")
    for photo in [day5.photo1, day5.photo2]:
        group1.add_photo(media=photo)
    await bot.send_media_group(
        media=group1.build()
    )
    await bot.send_photo(chat_id=user_id, photo=day5.photo3)
    await bot.send_photo(chat_id=user_id, photo=day5.photo4)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day6(user_id: int):
    await bot.send_message(chat_id=user_id, text=day6.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day6.video1, caption="On Guard\n6 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day6.text1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day6.text2, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day6.text3, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day6.photo1, caption=day6.caption1)
    await bot.send_photo(chat_id=user_id, photo=day6.photo2, caption=day6.caption2)
    await bot.send_photo(chat_id=user_id, photo=day6.photo3)
    await bot.send_photo(chat_id=user_id, photo=day6.photo4)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day7(user_id: int):
    await bot.send_message(chat_id=user_id, text=day7.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day7.video1, caption="Digest Zen\n7 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day7.text1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day7.text2, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day7.photo1, caption=day7.caption1)
    await bot.send_photo(chat_id=user_id, photo=day7.photo2)
    await bot.send_photo(chat_id=user_id, photo=day7.photo3)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day8(user_id: int):
    await bot.send_message(chat_id=user_id, text=day8.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day8.video1, caption="Breathe\n8 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day8.text1, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day8.photo1)
    await bot.send_photo(chat_id=user_id, photo=day8.photo2)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day9(user_id: int):
    await bot.send_message(chat_id=user_id, text=day9.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day9.video1, caption="Deep Blue\n9 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day9.text1)
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day9.photo1, caption=day9.caption1, parse_mode='MarkdownV2')
    await bot.send_photo(chat_id=user_id, photo=day9.photo2)
    await bot.send_photo(chat_id=user_id, photo=day9.photo3)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)

async def message_day10(user_id: int):
    await bot.send_message(chat_id=user_id, text=day10.greeting)
    await asyncio.sleep(VIDEO_AWAIT)
    await bot.send_video(chat_id=user_id, video=day10.video1, caption="Ладан\n10 день")
    await asyncio.sleep(TEXT_AWAIT)
    await bot.send_message(chat_id=user_id, text=day10.text1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=user_id, text=day10.text2, parse_mode='MarkdownV2')
    await asyncio.sleep(PHOTO_AWAIT)
    await bot.send_photo(chat_id=user_id, photo=day10.photo1)
    await bot.send_photo(chat_id=user_id, photo=day10.photo2)
    await asyncio.sleep(QUESTION_AWAIT)
    await bot.send_message(text=ShareText, reply_markup=ShareKeyboard)


daily_messages = [message_day1, message_day2, message_day3, message_day4, message_day5,
                  message_day6, message_day7, message_day8, message_day9, message_day10]