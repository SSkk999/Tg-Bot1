from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F ,Router



router = Router()
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(f"{message.from_user.full_name} koko jambo")

@router.message(Command('help'))
async def cmd_help(message:Message):
    await message.answer(f"{message.from_user.full_name} mayones,ketchup ") 


@router.message(F.photo)
async def get_photo(message:Message):
    await message.reply("leym skibidi yes yes ")

@router.message(F.text == "koko")
async def answer_koko(message:Message):
    await message.answer("jambo")
@router.message(F.text == "maks")
async def answer_koko(message:Message):
    await message.answer("leym")