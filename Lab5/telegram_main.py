#Бот для предоставление расписания преподавателей - @Andromaradbot

import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict
from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


from find import find_by_filter
from x import data_json

week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')

keyboard_to_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Меню 🔷")]], resize_keyboard=True)

TOKEN = "1521154065:AAEakIbgTMEDM0craYEgn_t8pMkNJl4aowI"
form_router = Router()


class Find(StatesGroup):
    mode = State()
    info_teacher = State()
    info_classroom = State()
    choose_teacher = State()
    choose_classroom = State()


@form_router.message(F.text == "Меню 🔷")
@form_router.message(CommandStart())
async def process_mode(message: Message, state: FSMContext) -> None:
    await state.set_state(Find.mode)
    await message.answer(
        f"Выберите действие",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text="Поиск по преподавателю"),
                    # KeyboardButton(text="Поиск по кабинету"),
                ]
            ],
            resize_keyboard=True,
        ),
    )


@form_router.message(Find.mode, F.text.lower() == "поиск по преподавателю")
async def process_get_teacher(message: Message, state: FSMContext) -> None:
    await state.update_data(mode="teacher")
    await state.set_state(Find.info_teacher)
    await message.answer(
        "Введите фамилию преподавателя:",
        reply_markup=keyboard_to_menu,
    )


@form_router.message(Find.info_teacher)
async def process_teachers(message: Message, state: FSMContext) -> None:
    info = message.text
    data = await state.get_data()

    variants, matched_lessons = find_by_filter(data_json, data['mode'], info)
    if len(variants) == 0:
        await state.clear()
        await message.answer(
            "Не найдено.",
            reply_markup=keyboard_to_menu,
        )
    elif len(variants) > 20:
        await state.clear()
        await message.answer(
            "Скишком много нашлось.",
            reply_markup=keyboard_to_menu,
        )
    elif len(variants) > 1:
        await state.update_data(variants=variants, lessons=matched_lessons)
        await state.set_state(Find.choose_teacher)
        answer = f"Найдено {len(variants)} преподавателей по вашему запросу\n\n"
        formatted_variants = [f"{i}. {t}" for i, t in enumerate(variants, start=1)]
        answer += '\n'.join(formatted_variants)
        await message.answer(
            answer,
            reply_markup=keyboard_to_menu,
        )
        await message.answer(
            "Кого показать?",
            reply_markup=keyboard_to_menu,
        )
    else:
        data = await state.update_data(variants=variants, lessons=matched_lessons)
        await state.clear()
        await text_teachers(message, data)


@form_router.message(Find.choose_teacher)
async def process_choose_teacher(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    variants = data["variants"]
    matched_lessons = data["lessons"]
    choose = int(message.text) - 1
    var = variants[choose]
    lessons = [lesson for lesson in matched_lessons if lesson["teacher"] == var]
    data = await state.update_data(variants=variants, lessons=lessons)
    await state.clear()
    await text_teachers(message, data)


async def text_teachers(message: Message, data):
    lessons = data["lessons"]
    lessons.sort(key=lambda les: (week.index(les['day']), les['lesson_n']))

    for day_name in week:
        lessons_day = [lesson for lesson in lessons if lesson["day"] == day_name]
        if lessons_day:
            answer = day_name + "\n"
            for l in lessons_day:
                answer += f'{l["lesson_n"]}| {l["classroom"]:6} | {l["group"]:8} | {l["subject"]} {l["mode"]}'
                if l["type"] == "числитель":
                    answer += " по числителям\n"
                elif l["type"] == "знаменатель":
                    answer += " по знаменателям\n"
                else:
                    answer += "\n"
            await message.answer(
                answer,
                reply_markup=keyboard_to_menu,
            )


async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(form_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
