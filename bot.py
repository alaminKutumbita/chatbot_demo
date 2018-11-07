from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('kutumbitaBot')
bot.set_trainer(ListTrainer)


def init_bot():
    for _file in os.listdir('files'):
        chats = open('files/' + _file, 'r').readlines()

        bot.train(chats)


def get_response(user_response):
    return str(bot.get_response(user_response))
