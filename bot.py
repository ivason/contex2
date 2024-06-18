from telebot import TeleBot
from model import init, get_placement


init_word, word_dict = init()
similarities = []
TOKEN = '5869374401:AAFtxKd5_2_hR0AMzsKzgikBLCutgfJxzPc'
bot = TeleBot(TOKEN)


print(len(word_dict))
print(init_word)


def get_string_words(similarities):
    end_string = ''
    for sim, count in similarities:
        end_string += f'{sim } {count}\n'
    return end_string




@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Вводите любые слова, чтобы играть. Используйте команду word')

@bot.message_handler(commands=['word'])
def word(message):
    global similarities
    if len(message.text.split(' ')) > 2:
        bot.send_message(message.chat.id, 'Больше 1 слова нельзя!')
        return
    _, word = message.text.split(' ')
    if word == init_word:
        bot.send_message(message.chat.id, 'Правильно!')
        return
    place = get_placement(word, word_dict)
    if place == -1:
        bot.send_message(message.chat.id, 'Очень далеко')
        return
    similarities.append((word, place))
    similarities.sort(key=lambda tup:tup[1])
    msg = get_string_words(similarities)
    bot.send_message(message.chat.id, msg)



    if __name__ == '__main__':
        bot.polling(none_stop=True)