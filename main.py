import pyowm
from pyowm.utils.config import get_default_config
import telebot

bot = telebot.TeleBot('2060133799:AAHP0fOR0wN5Pi89oj6h48lFfz2zbGFNUUo')

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('b58fbcb1deb95f901204c32fddc7f04b', config_dict)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        place = message.text
        observation = owm.weather_manager().weather_at_place(place)
        w = observation.weather

        response = f"Температура : {w.temperature('celsius').get('temp')} \n" \
                   f"Ощущается как : {w.temperature('celsius').get('feels_like')} \n" \
                   f"Скорость ветра: {w.wind().get('speed')} м/c. \n" \
                   f"На улице: {w.detailed_status}"
        print(w)
        bot.send_message(message.from_user.id, response)
    except Exception:
        bot.send_message(message.from_user.id, f"Не удалось получить информацию о погоде в  {message.text}")

bot.polling(none_stop=True, interval=0)

