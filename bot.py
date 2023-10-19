import nextcord
import colorama
import aiohttp
import requests
from nextcord.ext import commands, tasks
from nextcord import Intents
from colorama import Fore, Back, Style, init
import os
import sys
import asyncio
import time


intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents, help_command=None, case_insensitive=True)

botnormal = f"[{Fore.CYAN} - {Style.RESET_ALL}]"
boterror = f"[{Fore.RED} ! {Style.RESET_ALL}"
botwarn = f"[{Fore.YELLOW} : {Style.RESET_ALL}]"
botevent = f"[{Fore.GREEN} ? {Style.RESET_ALL}]"

os.system("cls")
print(botnormal + " Connection...")

def cogsload():
    for folder in ["track"]:
        for filename in os.listdir(folder):
            if filename.endswith(".py"):
                print(botnormal + f"{filename[:-3]} a été chargé avec succès")
                bot.load_extension(f"{folder}.{filename[:-3]}")
cogsload()

@bot.event
async def on_ready():
	os.system("cls")
	print(botnormal + " Connectée !")
	print(botnormal + " En tant que : "+ bot.user.name)
	time.sleep(3)

bot.run("token")
