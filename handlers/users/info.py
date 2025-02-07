from email.policy import default

from aiogram.types import Message
from loader import  router
from aiogram import F

@router.message(F.text=='rozigrish')
async def info(message :Message):
    message ='rozigrish'