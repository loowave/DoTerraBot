from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, StateFilter, Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from scheduler import schedule_messages_for_10_days
from messages import send_starting
import keyboards
import texts
import google_docs

redis = Redis(host='localhost', port=6379, db=0)
storage = RedisStorage(redis=redis)
dp = Dispatcher(storage=storage)


# Possible states
class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_consultant = State()
    fill_doterra_number = State()
    fill_country = State()
    fill_city = State()
    fill_time = State()
    fill_completed = State()


# Handler for "/start" command
@dp.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text=texts.start,
    )


# Handler for "/fillform" command
@dp.message(Command(commands='fillform'), StateFilter(default_state))
async def process_fillform_command(message: Message, state: FSMContext):
    await message.answer(text=texts.name)
    await state.set_state(FSMFillForm.fill_name)


# Handlere for "/fillform" command if form have been filled
@dp.message(Command(commands='fillform'), StateFilter(FSMFillForm.fill_completed))
async def process_fillform_command(message: Message):
    await message.answer(text=texts.fillform_after_filling)


# Handler for "/fillform" command if it's already being filled
@dp.message(Command(commands='fillform'), ~StateFilter(default_state))
async def process_fillform_command(message: Message):
    await message.answer(text=texts.fillform_while_filling)


# Handler for name
@dp.message(StateFilter(FSMFillForm.fill_name))
async def process_name_sent(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(text=texts.consultant)
    await state.set_state(FSMFillForm.fill_consultant)


# Handler for consultant
@dp.message(StateFilter(FSMFillForm.fill_consultant))
async def process_consultant_sent(message: Message, state: FSMContext):
    await state.update_data(consultant=message.text)
    await message.answer(text=texts.doterra_number)
    await state.set_state(FSMFillForm.fill_doterra_number)


# Handler for doterra number
@dp.message(StateFilter(FSMFillForm.fill_doterra_number), F.text.isdigit())
async def process_doterra_number_sent(message: Message, state: FSMContext):
    await state.update_data(doterra_number=int(message.text))
    await message.answer(
        text=texts.country,
        reply_markup=keyboards.CountryKeyboard
    )
    await state.set_state(FSMFillForm.fill_country)


# Handler for incorrect doterra number
@dp.message(StateFilter(FSMFillForm.fill_doterra_number))
async def warning_not_time(message: Message):
    await message.answer(
        text=texts.incorrect_number
    )


# Handler for country
@dp.callback_query(StateFilter(FSMFillForm.fill_country),
                   F.data.in_(['СНГ', 'Европа', 'Другое']))
async def process_country_press(callback: CallbackQuery, state: FSMContext):
    await state.update_data(country=callback.data)
    await callback.message.delete()
    await callback.message.answer(
        text=texts.city
    )
    await state.set_state(FSMFillForm.fill_city)


# Handler for incorrect country
@dp.message(StateFilter(FSMFillForm.fill_country))
async def warning_not_country(message: Message):
    await message.answer(
        text=texts.incorrect_country
    )


# Handler for city
@dp.message(StateFilter(FSMFillForm.fill_city))
async def process_city_sent(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    await message.answer(text=texts.time)
    await state.set_state(FSMFillForm.fill_time)


# Handler for incorrect city
@dp.message(StateFilter(FSMFillForm.fill_city))
async def warning_not_city(message: Message):
    await message.answer(
        text=texts.incorrect_city
    )


# Handler for time
@dp.message(StateFilter(FSMFillForm.fill_time),
            lambda message: message.text.isdigit() and 0 <= int(message.text) < 24)
async def process_time_sent(message: Message, state: FSMContext, apscheduler: AsyncIOScheduler):
    await state.update_data(time=int(message.text))
    await message.answer(text=texts.form_filled)
    await send_starting(message)
    await state.set_state(FSMFillForm.fill_completed)
    x = await state.get_data()
    await google_docs.update_google_sheets(x)
    schedule_messages_for_10_days(message.from_user.id, int(message.text), apscheduler=apscheduler)


# Handler for incorrect time
@dp.message(StateFilter(FSMFillForm.fill_time))
async def warning_not_time(message: Message):
    await message.answer(
        text=texts.incorrect_time
    )
