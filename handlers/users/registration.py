from aiogram.filters import Command
from aiogram.types import Message
from loader import  router, con, cursor
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import F

class Form_reg(StatesGroup):
    fio = State()
    numbers = State()
    email = State()
    age = State()

@router.message(F.text == 'registration')
async def start_reg(message: Message, state: FSMContext):
    id_user = message.chat.id
    status = True
    if id_user in con:
        cursor.execute('SELECT id FROM users WHERE id=(?) )', [id_user])
        con.commit()
    else:
        cursor.execute('INSERT INTO users (id) VALUES (?)', [id_user])
        con.commit()
    cursor.execute('SELECT status FROM start_reg WHERE status=(?) )', [status])
    con.commit()
    await state.set_state(Form_reg.fio)
    await message.answer('enter FIO', reply_markup=types.ReplyKeyboardRemove())

@router.message(Form_reg.fio)
async def get_fio(message: Message, state: FSMContext):


    data = await state.update_data(email=message.text)
    age = data['age']
    fio = data['fio']
    numbers = data['numbers']
    email = data['email']
    await state.set_state(Form_reg.age)
    await message.answer('enter email')
    con.cursor('INSERT INTO users WHERE email=(?)', [email])
    con.commit()
    await state.clear()
    await state.update_data(age=message.text)
    await state.set_state(Form_reg.age)
    await message.answer('enter age')
    con.cursor('INSERT INTO users WHERE age=(?)', [age])
    con.commit()
    await state.update_data(fio=message.text)
    await state.set_state(Form_reg.age)
    await message.answer('enter fio')
    con.cursor('INSERT INTO users WHERE fio=(?)', [fio])
    con.commit()
    await state.update_data(numbers=message.text)
    await state.set_state(Form_reg.age)
    await message.answer('enter numbers')
    con.cursor('INSERT INTO users WHERE numbers=(?)', [numbers])
    con.commit()


