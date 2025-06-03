# json_object = json.dumps(city_weather, indet=1)
# with open('weather_data.json', 'w') as f:
#     f.write(json_object)
# for x, y in city_weather.items():
#     print(x,y)





# import json
# import requests
# from telegram import Chat as TGChat
# API_key = 'de7cbe734e7e1b3827bdde85fc351fb2'
# TOKEN = "7005024345:AAEoA6Ov-nXKQKt3YN74RAZpo7zz4CnaG08"
# url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=de7cbe734e7e1b3827bdde85fc351fb2'
# url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=de7cbe734e7e1b3827bdde85fc351fb2'
# city = ("asdasdasd")
# city_weather = requests.get(url.format(city)).json()
#
# from telegram.ext import *
# from telegram.ext import Updater, CommandHandler, MessageHandler, filters
# # from telegram import ParseMode
# def get_weather(city):
#     status = False
#     city_weather = requests.get(url.format(city)).json()
#     if city_weather["code'"] == "404":
#         status = city_weather
#     else:
#         my_dict = {
#             "name": city_weather["name"],
#             "description": city_weather["weather"][0]["description"],
#             "icon": city_weather["weather"][0]["icon"],
#             "temperature": city_weather["main"]["temp"]
#         }
#         status = my_dict
#     return status

# def start(update, context):
#     update.message.reply_text("Hello! I am bot. What is your city")
# def handle_message(update, context):
#     city = update.message.text.strip()
#     data = get_weather(city)
#     for x in data:
#         update.message.reply_text(f"{x}  {data[x]}!")
#
# def main():
#     updater = Updater("TOKEN", use_context=True)
#
#     dp = updater.dispatcher
#
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()


# import json
# import requests
# import telebot
#
# API_key = 'de7cbe734e7e1b3827bdde85fc351fb2'
# TOKEN = "7005024345:AAEoA6Ov-nXKQKt3YN74RAZpo7zz4CnaG08"
# url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=de7cbe734e7e1b3827bdde85fc351fb2'
#
# bot = telebot.TeleBot(TOKEN)
#
# def get_weather(city):
#     status = False
#     city_weather = requests.get(url.format(city)).json()
#     if city_weather.get("cod") == "404":
#         status = city_weather
#     else:
#         my_dict = {
#             "name": city_weather["name"],
#             "description": city_weather["weather"][0]["description"],
#             "icon": city_weather["weather"][0]["icon"],
#             "temperature": city_weather["main"]["temp"]
#         }
#         status = my_dict
#     return status
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Hello! I am bot. What is your city")
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     city = message.text.strip()
#     data = get_weather(city)
#     if isinstance(data, dict):
#         for key, value in data.items():
#             bot.reply_to(message, f"{key}: {value}")
#     else:
#         bot.reply_to(message, "City not found")
#
# bot.polling()

# import telebot
# import requests
#
# API_key = "de7cbe734e7e1b3827bdde85fc351fb2"
# TOKEN = "7005024345:AAEoA6Ov-nXKQKt3YN74RAZpo7zz4CnaG08"
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Welcome to the Weather Bot! Please enter the city name:")
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     city = message.text.strip()
#     weather_data = get_weather(city)
#     if weather_data:
#         icon_url, temperature, description, city_name, country = weather_data
#         # Send weather information as text
#         response_message = f"{city_name}, {country}\n"
#         response_message += f"Temperature: {temperature:.2f} C\n"
#         response_message += f"Description: {description}"
#         bot.reply_to(message, response_message)
#
#         # Send weather icon as a photo
#         icon_image = requests.get(icon_url)
#         bot.send_photo(message.chat.id, icon_image.content)
#     else:
#         bot.reply_to(message, "City not found. Please enter a valid city name.")
#
# def get_weather(city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
#     res = requests.get(url)
#     if res.status_code == 404:
#         return None
#     weather = res.json()
#     icon_id = weather['weather'][0]['icon']
#     temperature = weather['main']['temp'] - 273.15
#     description = weather['weather'][0]['description']
#     city_name = weather['name']
#     country = weather['sys']['country']
#     icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
#     return icon_url, temperature, description, city_name, country
#
# bot.polling()






# -----------last-------------------
# import telebot
# import requests

# API_KEY = "de7cbe734e7e1b3827bdde85fc351fb2"
# TOKEN = "7005024345:AAEoA6Ov-nXKQKt3YN74RAZpo7zz4CnaG08"

# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Welcome to the Weather Bot! Please enter the city name:")

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     city = message.text.strip()
#     weather_data = get_weather(city)
#     if weather_data:
#         icon_url, temperature, description, city_name, country_code = weather_data
#         # Get the country flag emoji
#         country_flag = get_country_flag(country_code)
#         # Send weather information as text
#         response_message = f"{city_name}, {country_flag}\n"
#         response_message += f"Temperature: {temperature:.2f} C\n"
#         response_message += f"Description: {description}"
#         bot.reply_to(message, response_message)

#         # Send weather icon as a photo
#         icon_image = requests.get(icon_url)
#         bot.send_photo(message.chat.id, icon_image.content)
#     else:
#         bot.reply_to(message, "City not found. Please enter a valid city name.")

# def get_weather(city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         icon_id = data['weather'][0]['icon']
#         temperature = data['main']['temp'] - 273.15
#         description = data['weather'][0]['description']
#         city_name = data['name']
#         country_code = data['sys']['country']
#         icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
#         return icon_url, temperature, description, city_name, country_code
#     else:
#         return None

# def get_country_flag(country_code):
#     # Simple mapping of country codes to flag emojis
#     country_flags = {
#         "US": "🇺🇸",
#         "UK": "🇬🇧",
#         "FR": "🇫🇷",
#         # Add more country codes and flag emojis as needed
#     }
#     return country_flags.get(country_code, "🌍")  # Return globe emoji if country code not found

# bot.polling()



# import telebot
# import requests

# API_KEY = "de7cbe734e7e1b3827bdde85fc351fb2"
# # TOKEN = "7005024345:AAEoA6Ov-nXKQKt3YN74RAZpo7zz4CnaG08"
TOKEN = "8074064057:AAEoQGlH77P3x9RV46NmYFG4aBtcaDW9MIU"
# bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.reply_to(message, "Welcome to the Weather Bot! Please enter the city name:")

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     city = message.text.strip()
#     weather_data = get_weather(city)
#     if weather_data:
#         icon_url, temperature, description, city_name, country_code = weather_data
#         country_flag = get_country_flag(country_code)
#         response_message = f"{city_name}, {country_flag}\n"
#         response_message += f"Temperature: {temperature:.2f} C\n"
#         response_message += f"Description: {description}"
#         bot.reply_to(message, response_message)

#         icon_image = requests.get(icon_url)
#         bot.send_photo(message.chat.id, icon_image.content)
#     else:
#         bot.reply_to(message, "City not found. Please enter a valid city name.")

# def get_weather(city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         icon_id = data['weather'][0]['icon']
#         temperature = data['main']['temp'] - 273.15
#         description = data['weather'][0]['description']
#         city_name = data['name']
#         country_code = data['sys']['country']
#         icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
#         return icon_url, temperature, description, city_name, country_code
#     else:
#         return None

# def get_country_flag(country_code):
#     country_flags = {
#         "US": "🇺🇸",
#         "UK": "🇬🇧",
#         "FR": "🇫🇷",
#     }
#     return country_flags.get(country_code, "🌍")

# # ❗ Webhookni o'chirib tashlash
# bot.remove_webhook()

# # 🔁 Pollingni ishga tushirish
# bot.polling()


import telebot
from telebot import types
import requests

API_KEY = "de7cbe734e7e1b3827bdde85fc351fb2"
# TOKEN = "YOUR_BOT_TOKEN"  # <<< TOKENingizni shu yerga yozing
bot = telebot.TeleBot(TOKEN)

# Har bir foydalanuvchi uchun tilni saqlash
user_lang = {}

# Emojilar
WEATHER_EMOJIS = {
    "clear": "☀️",
    "clouds": "☁️",
    "rain": "🌧️",
    "drizzle": "🌦️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
}

COUNTRY_FLAGS = {
    "US": "🇺🇸", "UK": "🇬🇧", "FR": "🇫🇷", "UZ": "🇺🇿", "RU": "🇷🇺", "IN": "🇮🇳",
    "DE": "🇩🇪", "JP": "🇯🇵", "CN": "🇨🇳", "BR": "🇧🇷", "CA": "🇨🇦", "AU": "🇦🇺"
}

# Til matnlari
TEXT = {
    "uz": {
        "welcome": "🌤️ Ob-havo botiga xush kelibsiz!\n\nShahar nomini yozing yoki 📍 joylashuvingizni yuboring.",
        "language": "Iltimos, tilni tanlang:",
        "not_found": "⚠️ Shahar topilmadi. Iltimos, shahar nomini to‘g‘ri kiriting.",
        "weather": "Ob-havo",
    },
    "ru": {
        "welcome": "🌤️ Добро пожаловать в погодный бот!\n\nВведите название города или отправьте 📍 вашу геолокацию.",
        "language": "Пожалуйста, выберите язык:",
        "not_found": "⚠️ Город не найден. Пожалуйста, введите правильное название.",
        "weather": "Погода",
    },
    "en": {
        "welcome": "🌤️ Welcome to the Weather Bot!\n\nPlease type a city name or send your 📍 location.",
        "language": "Please select a language:",
        "not_found": "⚠️ City not found. Please enter a valid city name.",
        "weather": "Weather",
    }
}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇺🇸 English")
    bot.send_message(message.chat.id, TEXT["en"]["language"], reply_markup=markup)


@bot.message_handler(func=lambda m: m.text in ["🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇺🇸 English"])
def set_language(message):
    lang = "uz" if "O‘zbek" in message.text else "ru" if "Русский" in message.text else "en"
    user_lang[message.chat.id] = lang

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    location_button = types.KeyboardButton("📍 Share Location", request_location=True)
    back_button = types.KeyboardButton("🔙 Back")
    markup.add(location_button, back_button)

    bot.send_message(message.chat.id, TEXT[lang]["welcome"], reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == "🔙 Back")
def back_to_language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("🇺🇿 O‘zbekcha", "🇷🇺 Русский", "🇺🇸 English")
    bot.send_message(message.chat.id, TEXT["en"]["language"], reply_markup=markup)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    lang = user_lang.get(message.chat.id, 'en')
    if message.location:
        lat = message.location.latitude
        lon = message.location.longitude
        weather_data = get_weather_by_coords(lat, lon, lang)

        if weather_data:
            send_weather_info(message.chat.id, weather_data, lang)
        else:
            bot.send_message(message.chat.id, TEXT[lang]["not_found"])


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_city(message):
    lang = user_lang.get(message.chat.id, 'en')
    city = message.text.strip()
    weather_data = get_weather_by_city(city, lang)

    if weather_data:
        send_weather_info(message.chat.id, weather_data, lang)
    else:
        bot.send_message(message.chat.id, TEXT[lang]["not_found"])


def get_weather_by_city(city, lang):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang={lang}"
    return fetch_weather(url)


def get_weather_by_coords(lat, lon, lang):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang={lang}"
    return fetch_weather(url)


def fetch_weather(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        icon_id = data['weather'][0]['icon']
        temperature = data['main']['temp'] - 273.15
        description = data['weather'][0]['description']
        city_name = data['name']
        country_code = data['sys']['country']
        icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        return icon_url, temperature, description, city_name, country_code
    else:
        return None


def get_weather_emoji(description):
    for key in WEATHER_EMOJIS:
        if key in description.lower():
            return WEATHER_EMOJIS[key]
    return "🌈"


def send_weather_info(chat_id, weather_data, lang):
    icon_url, temp, desc, city, country = weather_data
    flag = COUNTRY_FLAGS.get(country, "🌍")
    emoji = get_weather_emoji(desc)

    msg = f"<b>{city}, {flag}</b>\n"
    msg += f"{emoji} <b>{desc.capitalize()}</b>\n"
    msg += f"🌡️ <b>{temp:.1f}°C</b>"

    bot.send_photo(chat_id, icon_url, caption=msg, parse_mode="HTML")


import time

# Webhookni o‘chirib, pollingni ishga tushiramiz
bot.remove_webhook()

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=60)
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(5)
