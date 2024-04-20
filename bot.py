#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import requests
from bs4 import BeautifulSoup
import random
import asyncio
import config
from telebot.async_telebot import AsyncTeleBot
bot = AsyncTeleBot(config.token)



# Handle '/start' and '/help'

@bot.message_handler(commands=['help', 'start']) 
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am MarauderBot.
now,i can only tell you jokes on russian,write the command /joke to see\
""")
    






@bot.message_handler(commands=['joke'])
async def get_random_joke(message):
    url = 'https://www.anekdot.ru/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        jokes = soup.find_all(class_='text')
        random_joke = random.choice(jokes).text.strip()
    else:
        print("Failed to retrieve jokes. Status code:", response.status_code)
        return

    await joke(message, random_joke)

async def joke(message, joke_text):
    await bot.reply_to(message, joke_text)

async def info(message):
    await bot.reply_to(message, '''
Hello there!
I was coded with a lot of love on a good Python IDE. I'm here to help you get started, although I'm just a testing bot for now. But I'll get better over time.
''')

asyncio.run(bot.polling())