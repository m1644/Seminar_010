
import telebot
from telebot import types


API_TOKEN = 'YOU TOKKEN'

bot = telebot.TeleBot(API_TOKEN)

cell = [' ' for x in range(0, 28)]
user_id = ''
candy = 101

def board(cell):
    candy_board = telebot.types.InlineKeyboardMarkup()
    candy_board.row(telebot.types.InlineKeyboardButton(f'{cell[0]}', callback_data='0'),
                    telebot.types.InlineKeyboardButton(f'{cell[1]}', callback_data='1'),
                    telebot.types.InlineKeyboardButton(f'{cell[2]}', callback_data='2'),
                    telebot.types.InlineKeyboardButton(f'{cell[3]}', callback_data='3'),
                    telebot.types.InlineKeyboardButton(f'{cell[4]}', callback_data='4'),
                    telebot.types.InlineKeyboardButton(f'{cell[5]}', callback_data='5'),
                    telebot.types.InlineKeyboardButton(f'{cell[6]}', callback_data='6'))
    
    candy_board.row(telebot.types.InlineKeyboardButton(f'{cell[7]}', callback_data='7'),
                    telebot.types.InlineKeyboardButton(f'{cell[8]}', callback_data='8'),
                    telebot.types.InlineKeyboardButton(f'{cell[9]}', callback_data='9'),
                    telebot.types.InlineKeyboardButton(f'{cell[10]}', callback_data='10'),
                    telebot.types.InlineKeyboardButton(f'{cell[11]}', callback_data='11'),
                    telebot.types.InlineKeyboardButton(f'{cell[12]}', callback_data='12'),
                    telebot.types.InlineKeyboardButton(f'{cell[13]}', callback_data='13'))
    
    candy_board.row(telebot.types.InlineKeyboardButton(f'{cell[14]}', callback_data='14'),
                    telebot.types.InlineKeyboardButton(f'{cell[15]}', callback_data='15'),
                    telebot.types.InlineKeyboardButton(f'{cell[16]}', callback_data='16'),
                    telebot.types.InlineKeyboardButton(f'{cell[17]}', callback_data='17'),
                    telebot.types.InlineKeyboardButton(f'{cell[18]}', callback_data='18'),
                    telebot.types.InlineKeyboardButton(f'{cell[19]}', callback_data='19'),
                    telebot.types.InlineKeyboardButton(f'{cell[20]}', callback_data='20'))
    
    candy_board.row(telebot.types.InlineKeyboardButton(f'{cell[21]}', callback_data='21'),
                    telebot.types.InlineKeyboardButton(f'{cell[22]}', callback_data='22'),
                    telebot.types.InlineKeyboardButton(f'{cell[23]}', callback_data='23'),
                    telebot.types.InlineKeyboardButton(f'{cell[24]}', callback_data='24'),
                    telebot.types.InlineKeyboardButton(f'{cell[25]}', callback_data='25'),
                    telebot.types.InlineKeyboardButton(f'{cell[26]}', callback_data='26'),
                    telebot.types.InlineKeyboardButton(f'{cell[27]}', callback_data='27'))
    return candy_board

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🎲Играть🎲')
    markup.add(item1)
    bot.send_message(message.chat.id, '''Привет! Это игра "🍬101🍬 конфета"! 
Основные правила игры: 
На кону в игре 🍬101🍬 конфета, за один ход ты можешь взять не более 🍬28🍬 штук! 
Победитель забирает ВСЁ🍬🍭🍬'''.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def play(message):
    global cell, candy
    cell = [x for x in range(1, 29)]
    
    if message.text == '🎲Играть🎲':
        bot.send_message(message.chat.id, f'На кону конфет 🍬{candy}🍬', reply_markup=board(cell))
    else:
        bot.send_message(message.chat.id, 'Упс...')
        
@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global cell, user_id, candy
    data = query.data
    data = int(data) + 1
    if candy > 0 and candy <= 101:
        user_id = query.from_user.id
        candy = candy - data
        if candy > 0 and candy < 101:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=f'На кону конфет 🍬{candy}🍬', reply_markup=board(cell))
        elif candy == 0:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=f'Игра окончена, все конфеты выиграл {user_id}🍬🍭🍬')
            candy = 101
        else:
            candy < 0
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=f'Конфет не осталось 🍬{candy}🍬, ты взял много!\nДавай сначала...(/start)')
            candy = 101    
    return callback_func
    
print('start bot')
      
bot.polling(none_stop=True)
