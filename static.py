import re
import sqlite3 #модуль sqlite
import discord
from discord import emoji
from discord import embeds
from discord import message
from discord import member
from discord import channel #модуль discord api
from discord.ext import commands
from discord.ext.commands import context
from discord.ext.commands.core import command #необходимый класс для обработки команд
from discord_components import DiscordComponents, Button, ButtonStyle, component, interaction
from requests.models import Response
from tabulate import tabulate #удобный модуль для рисования таблиц
import random
import asyncio
from asyncio import sleep
from discord.ext.commands import Bot
import os
import requests
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import io
from random import choice
from asyncio import TimeoutError as AsyncTimeoutError
import aiohttp
import discord
import datetime
import warnings
from discord_components import DiscordComponents, Select, SelectOption, Button, ButtonStyle
from discord.utils import get
import random, string
from discord.ext.commands import cooldown
import json
import requests
from discord.ext.commands import has_permissions
import time
import smtplib

# Черный список айди не желательных серверов и пользывателей ;)
whitelistuserscommand = ["727450233449218108", "835650277515460609", "696635462625918976"]
забратьрольучастника = ["901458173389602866"]

t22 = 1

Borodach = ['727450233449218108']
dexstray = ['835650277515460609']

warnings.filterwarnings("ignore", category=DeprecationWarning)
client = commands.Bot(command_prefix="_")
intents = discord.Intents.all()

conn = sqlite3.connect("bot.db") # или :memory:
cursor = conn.cursor()

@client.event
async def on_ready():
    DiscordComponents(client)
    cursor.execute("""CREATE TABLE IF NOT EXISTS shop (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT    UNIQUE
                 NOT NULL,
    name TEXT    UNIQUE
                 NOT NULL,
    cost INTEGER NOT NULL
                 UNIQUE
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id        INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname  TEXT    UNIQUE
                      NOT NULL,
    mention   TEXT    UNIQUE
                      NOT NULL,
    money     INTEGER,
    rep_rank  TEXT,
    inventory TEXT,
    lvl       INTEGER,
    xp        INTEGER
    )""")

    cursor.execute("""CRTATE TABLE IF NOT EXISTS buyers (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
    buyers TEXT    UNIQUE
                   NOT NULL
    )""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS phone (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname2 TEXT    NOT NULL
                      UNIQUE,
    phone     INTEGER NOT NULL
                      CONSTRAINT [+71111111111] UNIQUE
    )""")

    cursor.execute('''CREATE RABLE IF NOT EXISTS servers (
    id INTEGER PRIMARY KEY AUTOINCREMENT
        )''')
conn.commit()

bot = commands.Bot(command_prefix="_", intents=intents)#в строчке command_prefix можно указать любые знак, букву, слово, словосочетания и т.д.
bot.session = aiohttp.ClientSession()
#Здесь будет логика вашего бота
bot.remove_command('help')


# You can set default values, if u want
# default_rooms_initted = False
# default_room_category_id = 804067147391172658
# default_room_creator_id = 927254214554554398

# room_category = 804067147391172658
# room_creator = 927254214554554398

# # https://discordpy.readthedocs.io/en/latest/api.html#discord.abc.GuildChannel.delete
# async def delete_channel(guild, channel_id):
#         channel = guild.get_channel(channel_id)
#         await channel.delete()

# # https://discordpy.readthedocs.io/en/latest/api.html#discord.Guild.create_voice_channel
# async def create_voice_channel(guild, channel_name):
#         channel = await guild.create_voice_channel(channel_name, category=room_category)
#         return channel

# def init_rooms():
#     if default_room_category_id != -1:
#         category_channel = bot.get_channel(default_room_category_id)
#         if category_channel:
#             global room_category
#             room_category = category_channel

#     if default_room_creator_id != -1:
#         create_channel = bot.get_channel(default_room_creator_id)
#         if create_channel:
#             global room_creator
#             room_creator = create_channel
  
#     global default_rooms_initted
#     default_rooms_initted = True



# # https://discordpy.readthedocs.io/en/latest/api.html#discord.on_voice_state_update
# @bot.event
# async def on_voice_state_update(member, before, after):
#     if not default_rooms_initted:
#         init_rooms()

#     if not room_category:
#         print("Set 'Temp rooms category' id first (temp_category_set)")
#         return False

#     if not room_creator:
#         print("Set 'Temp rooms creator' id first (temp_rooms_set)")
#         return False

#     if member.bot:
#         return False
  
#     # If user joined to the room creator channel
#     if after.channel == room_creator:
#         channel = await create_voice_channel(after.channel.guild, f'{member.name} room') # create new voice channel in temp rooms category
#         if channel is not None: # if we successfully created our new voice room
#             await member.move_to(channel) # move member to new room
#             await channel.set_permissions(member, manage_channels=True) # set perm-s to the member
  
#     # If user leaved temp room
#     if before.channel is not None:
#         if before.channel != room_creator and before.channel.category == room_category:
#             if len(before.channel.members) == 0:
#                 await delete_channel(before.channel.guild, before.channel.id)


@bot.event
async def on_member_join(ctx):
    channel = bot.get_channel(927261007833874483)
    await channel.edit(name = f"👥︱людей:{ctx.guild.member_count}")

@bot.event
async def on_member_remove(ctx):
    channel = bot.get_channel(927261007833874483)
    await channel.edit(name = f"👥︱людей:{ctx.guild.member_count}")





@bot.command()
async def addserverB(ctx):
    if not str(ctx.author.id) in Borodach:
        return
    else:
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            cursor.execute(f"INSERT INTO servers VALUES ({ctx.guild.id}, '{ctx.guild.name}')")#вводит все данные об сервере в БД
                
            url1 = str(ctx.author.avatar_url)[:-10]
            emb = discord.Embed(title = 'Cервер:', color = discord.Color.green())
            
            emb.add_field( name = 'Успешно занесен в базу данных:', value = 'Спасибо за покупку!')
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {ctx.guild.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)
        else:
            await ctx.send('Сервер находиться в базе данных!')
        conn.commit()#применение изменений в БД


@bot.command()
async def addserverD(ctx):
    if not str(ctx.author.id) in dexstray:
        return
    else:
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            cursor.execute(f"INSERT INTO servers VALUES ({ctx.guild.id}, '{ctx.guild.name}')")#вводит все данные об сервере в БД
                
            url1 = str(ctx.author.avatar_url)[:-10]
            emb = discord.Embed(title = 'Cервер:', color = discord.Color.green())
            
            emb.add_field( name = 'Успешно занесен в базу данных:', value = 'Спасибо за покупку!')
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {ctx.guild.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)
        else:
            await ctx.send('Сервер находиться в базе данных!')
        conn.commit()#применение изменений в БД


@bot.command()
async def blacklistB(ctx, member: discord.Member):
    if not str(ctx.author.id) in Borodach:
        return
    else:
        cursor.execute(f"SELECT id FROM blacklist where id={member.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            cursor.execute(f"INSERT INTO blacklist VALUES ({member.id}, '{member.name}')")#вводит все данные об сервере в БД
            
            url1 = str(member.avatar_url)[:-10]
            emb = discord.Embed(title = 'Blacklist:', color = discord.Color.red())
            
            emb.add_field( name = f'Участник {member.name}', value = 'Занесен в Blacklist!')
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)
        else:
            await ctx.send(f'Участник {member.name}, уже находиться в Blacklist')
        conn.commit()#применение изменений в БД


@bot.command()
async def blacklistD(ctx, member: discord.Member):
    if not str(ctx.author.id) in dexstray:
        return
    else:
        cursor.execute(f"SELECT id FROM blacklist where id={member.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            cursor.execute(f"INSERT INTO blacklist VALUES ({member.id}, '{member.name}')")#вводит все данные об сервере в БД
            
            url1 = str(member.avatar_url)[:-10]
            emb = discord.Embed(title = 'Blacklist:', color = discord.Color.red())
            
            emb.add_field( name = f'Участник {member.name}', value = 'Занесен в Blacklist!')
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)
        else:
            await ctx.send(f'Участник {member.name}, уже находиться в Blacklist')
        conn.commit()#применение изменений в БД

##################################################################################################################################### ставки
@bot.command()
@commands.has_permissions( administrator = True )
async def ставка(ctx):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            emb = discord.Embed(title = 'Ставки:', color = discord.Color.blue())
            emb.add_field( name = f'{ctx.author.name}', value = 'На кого хотите поставить?')
            message = await ctx.send(embed = emb)
            await message.add_reaction('💜')
            await message.add_reaction('🧡')
            await message.add_reaction('💚')

            def check(reaction, user):
                    return str(reaction.emoji) == '💜' and user != bot.user

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=20, check=check)
                emb = discord.Embed(title = 'Ставка на 💜', color = discord.Color.purple())
                emb.add_field( name = f'{ctx.author.name}', value = 'Сколько хотите поставить?')
                message = await ctx.send(embed = emb)
                await message.add_reaction('2️⃣')
                await message.add_reaction('5️⃣')
                await message.add_reaction('🔟')
            except asyncio.TimeoutError:
        
                await ctx.send("**Время ожидания вышло!**")
            else:
                def check(reaction, user):
                    return str(reaction.emoji) == '2️⃣' and user != bot.user
            try:
                for row in cursor.execute(f"SELECT money FROM users where id={ctx.author.id}"):
                    money = row[0]
                    cost = 2000
                    if money >= cost:#если у вас достаточно денег,то...
                            money -=cost
                            uid=ctx.author.id
                            for row in cursor.execute(f"SELECT money FROM users where id={ctx.author.id}"):
                                cursor.execute('UPDATE users SET money=? where id=?',(money -2000,uid))
                            reaction, user = await bot.wait_for('reaction_add', timeout=20, check=check)
                            emb = discord.Embed(title = 'Ставка принята!', color = discord.Color.purple())
                            emb.add_field( name = f'{ctx.author.name}', value = 'Спасибо за ставку на Розовых!')
                            message = await ctx.send(embed = emb)
                    else:
                        money < cost
                        emb = discord.Embed(title = 'Ставка НЕ принята!', color = discord.Color.purple())
                        emb.add_field( name = f'{ctx.author.name}', value = 'У вас не достаточно средств!')
                        message = await ctx.send(embed = emb)
            except asyncio.TimeoutError:
                await ctx.send("**Время ожидания вышло!**")

            else:
                def check(reaction, user):
                    return str(reaction.emoji) == '5️⃣' and user != bot.user

            try:
                for row in cursor.execute(f"SELECT money FROM users where id={ctx.author.id}"):
                    money = row[0]
                    cost = 5000
                    if money >= cost:#если у вас достаточно денег,то...
                            money -=cost
                            uid=ctx.author.id
                            for row in cursor.execute(f"SELECT money FROM users where id={ctx.author.id}"):
                                cursor.execute('UPDATE users SET money=? where id=?',(money -5000,uid))
                            reaction, user = await bot.wait_for('reaction_add', timeout=20, check=check)
                            emb = discord.Embed(title = 'Ставка принята!', color = discord.Color.purple())
                            emb.add_field( name = f'{ctx.author.name}', value = 'Спасибо за ставку на Розовых!')
                            message = await ctx.send(embed = emb)
                    else:
                        money < cost
                        emb = discord.Embed(title = 'Ставка НЕ принята!', color = discord.Color.purple())
                        emb.add_field( name = f'{ctx.author.name}', value = 'У вас не достаточно средств!')
                        message = await ctx.send(embed = emb)
            except asyncio.TimeoutError:
                await ctx.send("**Время ожидания вышло!**")

            else:
                def check(reaction, user):
                    return str(reaction.emoji) == '🔟' and user != bot.user
            try:
                for row in cursor.execute(f"SELECT money FROM users where id={ctx.author.id}"):
                    money = row[0]
                    cost = 10000
                    if money >= cost:#если у вас достаточно денег,то...
                            money -=cost
                            uid=ctx.author.id
                            for row in cursor.execute(f"SELECT money FROM users where id={ctx.author.id}"):
                                cursor.execute('UPDATE users SET money=? where id=?',(money -10000,uid))
                            reaction, user = await bot.wait_for('reaction_add', timeout=20, check=check)
                            emb = discord.Embed(title = 'Ставка принята!', color = discord.Color.purple())
                            emb.add_field( name = f'{ctx.author.name}', value = 'Спасибо за ставку на Розовых!')
                            message = await ctx.send(embed = emb)
                    else:
                        money < cost
                        emb = discord.Embed(title = 'Ставка НЕ принята!', color = discord.Color.purple())
                        emb.add_field( name = f'{ctx.author.name}', value = 'У вас не достаточно средств!')
                        message = await ctx.send(embed = emb)
            except asyncio.TimeoutError:
                await ctx.send("**Время ожидания вышло!**")    
##################################################################################################################################### напоминание
@bot.event
async def on_ready():
    TIMEOUT = 427398
    ID_CHANNEL = 921094923569217577
    channel = bot.get_channel(ID_CHANNEL)
    while True:
        await asyncio.sleep(TIMEOUT)
        await channel.send('**Игры начнутся сегодня в 15:10**')
##################################################################################################################################### 1 игра - 2 игра
@bot.event
async def on_ready():
    TIMEOUT = 429328
    ID_CHANNEL = 922467213762523186
    channel = bot.get_channel(ID_CHANNEL)
    while True:
        await asyncio.sleep(TIMEOUT)
        msg = await channel.send("Дуэль: **Кто первый?**")
        await msg.add_reaction('🎨')
    
        def check(reaction, user):
                return str(reaction.emoji) == '🎨' and user != bot.user
    
        try:
            # Timeout parameter is optional but sometimes can be useful
            reaction, user = await bot.wait_for('reaction_add', timeout=5, check=check)

            # Will wait until a user reacts with the specified checks then continue on with the code
            await channel.send(f"Поздравляю {user.name} ты Победил(а)!")
        except asyncio.TimeoutError:
        
            # when wait_for reaches specified timeout duration (in this example it is 30 seconds)
            await channel.send("**Время вышло :(**")
##################################################################################################################################### 3 игра - 4 игра
\
##################################################################################################################################### 5 игра - 6 игра
\
##################################################################################################################################### 7 игра - 8 игра
\
##################################################################################################################################### 9 игра - 10 игра
\
#####################################################################################################################################

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready to go!")

async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with bot.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False

@bot.command()
async def timeout(ctx: commands.Context, member: discord.Member, until: int):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
        return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            handshake = await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=until)
    if handshake:
         return await ctx.send(f"Участник {member.name} был лишен голоса на {until} минуты/минут.")
    await ctx.send("Something went wrong")


# async def selectboxTesting(ctx):
#     await ctx.send(content = "Select an option!", components = [Select(
#                                                   placeholder = 'Select Sothing!',
#                                                   options= [
#                                                       SelectOption(label = "Insquad", value = "1", description = "Purple Team", emoji = '🟣'),
#                                                       SelectOption(label = "Sunrise", value = "2", description = "Orange Team", emoji = '🟠'),
#                                                       SelectOption(label = "Sunrise", value = "3", description = "Green Team", emoji = '🟢'),
#                                                       SelectOption(label = "Rainbow", value = "4", description = "Rainbow Role", emoji = '🌈')
#                                                   ],
#                                                   custom_id='SelectTesting'
#     )])

#     interaction = await bot.wait_for('select_option', check=lambda inter: inter.custom_id == 'SelectTesting' and inter.user == ctx.author)
#     res = interaction.values[0]

#     purple = discord.utils.get(ctx.message.guild.roles, name="Розовые")
#     orange = discord.utils.get(ctx.message.guild.roles, name="Оранжевые")
#     green = discord.utils.get(ctx.message.guild.roles, name="Зеленые")

#     if res == '1':
#         await member.add_roles(purple)
#     elif res == '2':
#         await member.add_roles(orange)
#     elif res == '3':
#         await member.add_roles(green)

# @bot.command()
# async def testing(ctx):
#     await selectboxTesting(ctx)


@bot.event
async def on_member_join(ctx):
    cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
    if cursor.fetchone()==None:#Если не существует
        return
    else:
        img = Image.new('RGBA', (550, 130), '#f1c40f00')
        url = str(ctx.author.avatar_url)[:-10]

    response = requests.get(url, stream = True)
    card_channel = bot.get_channel(908371587621867540)

    if not response:
        await card_channel.send(f'{ctx.author.name} Тебе придется поставить аватарку, чтобы увидеть приветственную карту!')
        return
    else:
        response = Image.open(io.BytesIO(response.content))

        response = response.convert('RGBA')
        response = response.resize((100, 100), Image.ANTIALIAS)

        img.paste(response, (15, 15, 115, 115))

        idraw = ImageDraw.Draw(img)
        name = ctx.author.name
        tag = ctx.author.discriminator

        headline = ImageFont.truetype('days2.ttf', size = 20)
        undertext = ImageFont.truetype('days2.ttf', size = 12)
        ps = ImageFont.truetype('days2.ttf', size = 15)
        headline3 = ImageFont.truetype('days2.ttf', size = 10)

        idraw.text((145, 15), f'Добро Пожаловать {name}', font = headline)
        idraw.text((145, 50), f'На сервер {ctx.guild.name}', font = ps)
        idraw.text((145, 75), f'Ты {ctx.guild.member_count}th Участник', font = ps)
        idraw.text((145, 105), f'ID: {ctx.author.id}', font = undertext)
        img.save('helloy.png')

        await card_channel.send(file = discord.File(fp = 'helloy.png'))


@bot.command(pass_context=True)
async def вопрос(ctx, *, response):
    if not str(ctx.author.id) in Borodach:
        return
    else:
            await ctx.channel.purge(limit = 1)
            emb = discord.Embed(title = f'Опрос', color = discord.Color.red())

            emb.add_field( name = 'Участников', value = f'{response}')
            emb.set_thumbnail(url = 'https://i.ibb.co/8cD6Z0n/ece71c6d2eba5ee46e3246419882d86a-1.png')
            message = await ctx.send(embed = emb)
            await message.add_reaction('👍🏿')
            await message.add_reaction('👎🏿')

@bot.command(pass_context=True)
@cooldown(1, 15)  # 1000 second cooldown
@commands.dm_only()
async def ответ(ctx, *, response):
    sh = "" + ('').join(random.choices(string.ascii_letters + string.digits, k=8))
    tag = ctx.author.discriminator
    owner = bot.get_user(727450233449218108)
    emb = discord.Embed(title = f'Ответ', color = discord.Color.green())

    emb.add_field( name = f'Участника - {ctx.author.name}', value = f'Ответ принят на рассмотрение!')
    emb.add_field( name = f'Ваш серийный номер "{sh}"', value = f'ID: {ctx.author.id}')
    emb.set_thumbnail(url = 'https://i.ibb.co/8cD6Z0n/ece71c6d2eba5ee46e3246419882d86a-1.png')
    await ctx.send(embed = emb)
    await owner.send(f"{ctx.author.name}#{tag} - {response}. Серийный номер: {sh}")

@bot.command()
async def tets(ctx, member: discord.Member, *, response2):
    cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
    if cursor.fetchone()==None:#Если не существует
        return
    else:
        await ctx.send('Запрос выполняеться подождите немного... 🕓')
        img = Image.new('RGBA', (1800, 2543), '#f1c40f00')
        url = ('https://i.ibb.co/Kq7q2Qk/file-3503.jpg')

    response = requests.get(url, stream = True)

    if not response:
        await ctx.send(f'{ctx.author.name} Тебе придется поставить аватарку, чтобы увидеть приветственную карту!')
        return
    else:
        response = Image.open(io.BytesIO(response.content))

        response = response.convert('RGBA')
        response = response.resize((1800, 2543))

        img.paste(response, (1, 1))

        idraw = ImageDraw.Draw(img)
        name = ctx.author.name
        tag = ctx.author.discriminator

        def check(m):
            return m.content == f"{response}" and m.channel == channel
        msg = await bot.wait_for("message", check=check)

        ФИО = ImageFont.truetype('days2.ttf', size = 48)

        idraw.text((569, 465), f'{response2}', font = ФИО, fill = '#000')
        idraw.text((569, 542), f'{response2}', font = ФИО, fill = '#000')

        idraw.text((599, 465), f'{msg.member}', font = ФИО, fill = '#000')
        idraw.text((599, 542), f'{msg.member}', font = ФИО, fill = '#000')

        # idraw.text((145, 75), f'Ты {ctx.guild.member_count}th Участник', font = ps)
        # idraw.text((145, 105), f'ID: {ctx.author.id}', font = undertext)
               
        img.save('svadba.png')

        await ctx.send(file = discord.File(fp = 'svadba.png'))

@bot.command()
@cooldown(1, 50)
async def жалоба(ctx, member: discord.Member, *, response):
    owner = bot.get_user(727450233449218108)
    emb = discord.Embed(title = f'Жалоба', color = discord.Color.blue())
    url = str(ctx.author.avatar_url)[:-10]

    emb.add_field( name = f'Жалоба на - {member}', value = f'Участником - {ctx.author.name}')
    emb.add_field( name = f'По Причине:', value = f'{response}')
    emb.set_thumbnail(url = url)
    await ctx.send(embed = emb)

    emb1 = discord.Embed(title = f'Жалоба', color = discord.Color.blue())
    url = str(ctx.author.avatar_url)[:-10]
    tag = ctx.author.discriminator

    emb1.add_field( name = f'Жалоба на - {member}', value = f'Участником - {ctx.author.name}#{tag}')
    emb1.add_field( name = f'По Причине:', value = f'{response}')
    emb1.set_thumbnail(url = url)

    message = await owner.send(embed = emb1)
    await message.add_reaction('👍')
    await message.add_reaction('👎')

    def check(reaction, user):
        return str(reaction.emoji) == '👍' and user != bot.user
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=86400, check=check)
        # добавление пользователя на которого пожаловались
        mem = bot.get_user(member.id)
        await timeout_user(user_id=member.id, guild_id=890976299579998288, until=1440)
        await ctx.send(f"Пользователь {member.name} был замучен на 1 день, по причине `{response}`")
        await mem.send(f"Вы были замучены на 1 день, по причине жалобы - `{response}` от пользователя {ctx.author.name}")
    except asyncio.TimeoutError:
        await ctx.send("**Время ожидания вышло!**")

    def check(reaction, user):
        return str(reaction.emoji) == '👎' and user != bot.user
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=86400, check=check)
        # добавление пользователя который пожаловался, в случаи если ложная жалоба
        auth = bot.get_user(ctx.author.id)
        await timeout_user(user_id=ctx.author.id, guild_id=890976299579998288, until=1440)
        await ctx.send(f"Пользователь {ctx.author.name} был замучен на 1 день, по причине `Ложна жалоба`")
        await auth.send("Вы были замучены на 1 день, по причине `Ложная жалоба`")
    except asyncio.TimeoutError:
            await ctx.send("**Время ожидания вышло!**")

@bot.command()
async def фейк(ctx, member: discord.Member, *, response):
		colour = {
			"time": (114, 118, 125),
			"content": (220, 221, 222)
		}

		size = {
			"title": 20,
			"time": 13
		}

		font = 'Whitney-Medium.otf'

		if not member:
			member = ctx.author

		img = Image.new('RGB', (500, 115), color = (54,57,63))
		titlefnt = ImageFont.truetype(font, size["title"])
		timefnt = ImageFont.truetype(font, size["time"])
		d = ImageDraw.Draw(img)
		if member.nick is None:
			txt = member.name
		else:
			txt = member.nick
		color = member.color.to_rgb()
		if color == (0, 0, 0):
			color = (255,255,255)
		d.text((90, 20), txt, font=titlefnt, fill=color)
		h, w = d.textsize(txt, font=titlefnt)
		time = datetime.datetime.utcnow().strftime("Today at %I:%M %p")
		d.text((90+h+10, 25), time, font=timefnt, fill=colour["time"])
		d.text((90, 25+w), response, font=titlefnt, fill=colour["content"])

		img.save('img.png')
		if member.is_avatar_animated():
			await member.avatar_url_as().save("pfp.gif")
			f2 = Image.open("pfp.gif")
		else:
			await member.avatar_url_as().save("pfp.png")
			f2 = Image.open("pfp.png")
		f1 = Image.open("img.png")
		f2.thumbnail((50, 55))
		f2.save("pfp.png")

		f2 = Image.open("pfp.png").convert("RGB")

		mask = Image.new("L", f2.size, 0)
		draw = ImageDraw.Draw(mask)
		draw.ellipse((0, 0, f2.size[0], f2.size[1]), fill=255)
		mask = mask.filter(ImageFilter.GaussianBlur(0))

		result = f2.copy()
		result.putalpha(mask)

		result.save('pfp.png')

		f2 = Image.open("pfp.png")

		f3 = f1.copy()
		f3.paste(f2, (20, 20), f2)
		f3.save("img.png")

		file = discord.File("img.png")
		await ctx.send(file=file)

		try:
			os.remove("pfp.gif")
			os.remove("pfp.png")
			os.remove("img.png")
			await ctx.channel.purge(limit = 1)
		except:
			pass

def setup(bot):	
	bot.add_cog(фейк(bot))

try:
	bot.add_cog(фейк)
except:
	pass

@bot.command()
async def роли(ctx):
    await ctx.channel.purge(limit = 1)
    emb = discord.Embed(title = 'Роли', color = discord.Color.gold())

    emb.add_field( name = 'Прогер Антоша', value = 'Роль @Borodach`a')
    emb.add_field( name = 'радуга', value = 'Меняет цвет ника раз в 10 сек.')
    emb.add_field( name = 'Создатель', value = 'Создатель сервера')
    emb.add_field( name = 'Mute', value = 'Роль замучегного человека')
    emb.add_field( name = 'Главный Админ', value = 'Главный Администратор сервера')
    emb.add_field( name = 'Админ', value = 'Администратор сервера')
    emb.add_field( name = 'Модератор', value = 'Модератор сервера')
    emb.add_field( name = 'Бета тестеры', value = 'Бета тестеры бота и других фичь')
    emb.add_field( name = 'Младший Модератор', value = 'Модератор с уменшеными возможностями')
    emb.add_field( name = 'Боты', value = 'Боты сервера')
    emb.add_field( name = 'Участника', value = 'Роль полностью верифецированного участника')
    emb.add_field( name = 'Верифицирован', value = 'Роль верифицированного пользователя')
    emb.add_field( name = 'Розовый', value = 'Команда Розовых')
    emb.add_field( name = 'Зеленый', value = 'Команда Зеленых')
    emb.add_field( name = 'Оранжевый', value = 'Команда Оранжевых')
    emb.set_thumbnail(url = 'https://i.ibb.co/D7GhCyj/discord-colors-3.jpg')

    await ctx.send(embed = emb)


@bot.command()
async def сервера(ctx):
    if not str(ctx.author.id) in whitelistuserscommand:
        await ctx.send('Эта команда предназначена не дня вас!')
        return
    pp = await ctx.send('''Бот запустился
------------------''')#сообщение о готовности
    for guild in bot.guilds:#т.к. бот для одного сервера, то и цикл выводит один сервер
        pp = print(guild.id)#вывод id сервера
        pp = serv=guild#без понятия зачем это
        await ctx.send(pp)
        for member in guild.members:#цикл, обрабатывающий список участников
            cursor.execute(f"SELECT id FROM users where id={member.id}")#проверка, существует ли участник в БД
            if cursor.fetchone()==None:#Если не существует
                cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 2000, 'S','[]',1,1,0)")#вводит все данные об участнике в БД
            else:#если существует
                pass
            conn.commit()#применение изменений в БД

@bot.command(pass_context=True)
async def hug(ctx):
    user = choice(ctx.message.channel.guild.members)
    await ctx.send(f'{ctx.message.author.mention} hugged {user.mention}')


@bot.event
async def on_member_join(member):
    if welcome_channel := member.guild.get_channel(908371587621867540):
        await welcome_channel.send(f"Привет, {member.mention} твой айди - {member.guild.name} наш сервер - {member.guild.name}")

@bot.command()
async def покупатели(ctx):
    if not str(ctx.author.id) in whitelistuserscommand:
        await ctx.send('Эта комманда предназначена не дня вас!')
        return
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
        return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:    
            table=[["id","buyers"]]
            for row in cursor.execute(f"SELECT id,buyers FROM buyers"):
                table.append([row[0],row[1]])
                await ctx.send(f">\n{tabulate(table)}")

@bot.command()
@commands.dm_only()
async def подтверждение(ctx):
    ctx.channel.type == discord.ChannelType.private
    await ctx.send(
        embed=discord.Embed(title="Отправь мне свой номер телефона, пример: **_номер** +380111111111, +71111111111, ..."),
    components=[
            Button(style=ButtonStyle.URL, label="Что за политика?", url="https://www.tiqets.com/ru/privacy-policy/")
        ]
    )
    

@bot.command()
async def сайт(ctx):
        cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
        if cursor.fetchone():#Если существует
            return
        else: 
            cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
            if cursor.fetchone()==None:#Если не существует
                return
            else:
                await ctx.send(
                embed=discord.Embed(title="В разработке!"),
                components=[
                    Button(style=ButtonStyle.URL, label="Наш официальный сайт", url="http://fumacrom.com/3CXdM"),
                    Button(style=ButtonStyle.green, label="Оставить отзыв о сайте", emoji="💬"),
            ]
        )

        revive = await bot.wait_for("button_click")
        if revive.channel == ctx.channel:
         if revive.component.label == "Оставить отзыв о сайте":
             await revive.edit_origin(
                 embed=discord.Embed(title="Отзыв"),
                 components=[
                    Button(style=ButtonStyle.green, label="Мне понравился сайт!", emoji="✅"),
                    Button(style=ButtonStyle.red, label="Мне не понравился сайт!", emoji="❌") 
                 ]
             )
        revive1 = await bot.wait_for("button_click")
        if revive1.channel == ctx.channel:
         if revive1.component.label == "Мне понравился сайт!":
             await revive1.edit_origin(content="Спасибо за отзыв!")
         else:
             await revive1.edit_origin(
                 embed=discord.Embed(title="Что тебе не понравилось?:"),
                 components=[
                     Button(style=ButtonStyle.red, label="Мне не понравилось оформление", emoji="❌"),
                     Button(style=ButtonStyle.red, label="Слишком простой", emoji="❌"),
                     Button(style=ButtonStyle.red, label="Не все анимации нормально работают", emoji="❌"),
                     Button(style=ButtonStyle.red, label="Сайт не открылся", emoji="❌"),
                     Button(style=ButtonStyle.red, label="Сыллки не работают", emoji="❌")
                 ]
             )

        revive2 = await bot.wait_for("button_click")
        if revive2.channel == ctx.channel:
         if revive2.component.label == "Мне не понравилось оформление":
             await revive2.edit_origin(content="Спасибо за отзыв мы примем меры!")
         if revive2.component.label == "Слишком простой":
            await revive2.edit_origin(content="Спасибо за отзыв мы примем меры!")
         if revive2.component.label == "Не все анимации нормально работают":
             await revive2.edit_origin(content="Спасибо за отзыв мы примем меры!")
         if revive2.component.label == "Сайт не открылся":
             await revive2.edit_origin(content="Спасибо за отзыв мы примем меры!")
         if revive2.component.label == "Сыллки не работают":
             await revive2.edit_origin(content="Спасибо за отзыв мы примем меры!")


@bot.command()
async def купить(ctx):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
        return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.send('''```css
            Привет друг сегоднешний прайс на ботов ты можешь увидеть ниже:
            @antosha22 - 500 RUB
            @antosha23 - Ждите релиза!
            @antosha24 - Ждите релиза!```''')

@bot.command()
@commands.has_permissions( administrator = True )
async def киквойс(ctx: commands.Context, user: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.send(f'{user.mention} Кикнут с {user.voice.channel.mention}')
            await user.move_to(None)


@bot.command(aliases = ['карточка', 'карта', 'моя карта'])
async def card_user(ctx):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            img = Image.new('RGBA', (390, 130), '#001a1a')
            url = str(ctx.author.avatar_url)[:-10]

            response = requests.get(url, stream = True)

            if not response:
                await ctx.send(f'{ctx.author.name} Тебе придется поставить аватарку, дружочек!')
                return
            else:
                await ctx.channel.purge(limit = 1)
                response = Image.open(io.BytesIO(response.content))

            response = response.convert('RGBA')
            response = response.resize((100, 100), Image.ANTIALIAS)

            img.paste(response, (15, 15, 115, 115))

            idraw = ImageDraw.Draw(img)
            name = ctx.author.name
            tag = ctx.author.discriminator

            headline = ImageFont.truetype('days2.ttf', size = 20)
            undertext = ImageFont.truetype('days2.ttf', size = 12)
            ps = ImageFont.truetype('days2.ttf', size = 15)
            headline3 = ImageFont.truetype('days2.ttf', size = 10)

            idraw.text((145, 15), f'{name}#{tag}', font = headline)
            idraw.text((145, 50), f'ID: {ctx.author.id}', font = undertext)
            idraw.text((145, 75), f'P.S - наш любимый\nдолбоебик', font = ps)
            idraw.text((375, 10), '. .\nA\nR\nA\nM\nI\nR\nA', '#ffff56', font = headline3)
            img.save('user_card.png')

            await ctx.send(file = discord.File(fp = 'user_card.png'))


@bot.command()
@commands.has_permissions( administrator = True )
async def mute( ctx, member: discord.Member, time: int):
    emb = discord.Embed(title="Участник Был Замучен!", colour=discord.Color.green())

    emb.set_author(name=member.name, icon_url=member.avatar_url )
    emb.set_footer(text="Модератор: {}".format(ctx.author.name ), icon_url=ctx.author.avatar_url )
    
    await ctx.send(embed=emb)
    muted_role = discord.utils.get(ctx.message.guild.roles, name="Mute")
    e1 = discord.utils.get(ctx.message.guild.roles, name="Участник")
    e2 = discord.utils.get(ctx.message.guild.roles, name="Верифицирован")
    await member.add_roles(muted_role)
    await member.remove_roles(e1)
    await member.remove_roles(e2)
    
    # Спим X секунд, перед тем как снять роль.
    await asyncio.sleep(time) 
    # Снимаем роль замученного.
    await member.remove_roles(muted_role)
    await member.add_roles(e2)



@bot.command()
@commands.has_permissions( administrator = True )            
async def mlmoderator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Младший Модератор')
            await member.add_roles(mlmoderator)
            emb = discord.Embed(title = 'Мл. Модератор:', color = discord.Color.orange())
            emb.add_field( name = f'{member.name}', value = 'Поздравляю с повышением!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions( administrator = True )            
async def moderator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Модератор')
            await member.add_roles(mlmoderator)
            emb = discord.Embed(title = 'Модератор:', color = discord.Color.orange())
            emb.add_field( name = f'{member.name}', value = 'Поздравляю с повышением!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions( administrator = True )            
async def administrator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Админ')
            await member.add_roles(mlmoderator)
            emb = discord.Embed(title = 'Администратор:', color = discord.Color.orange())
            emb.add_field( name = f'{member.name}', value = 'Поздравляю с повышением!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions( administrator = True )            
async def gladministrator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Главный Админ')
            await member.add_roles(mlmoderator)
            emb = discord.Embed(title = 'Главный Администратор:', color = discord.Color.orange())
            emb.add_field( name = f'{member.name}', value = 'Поздравляю с повышением!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)


##############################################################################################################################
@bot.command()
@commands.has_permissions( administrator = True )            
async def unmlmoderator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Младший Модератор')
            await member.remove_roles(mlmoderator)
            emb = discord.Embed(title = 'Мл. Модератор:', color = discord.Color.red())
            emb.add_field( name = f'{member.name}', value = 'Отобран!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions( administrator = True )            
async def unmoderator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Модератор')
            await member.remove_roles(mlmoderator)
            emb = discord.Embed(title = 'Модератор:', color = discord.Color.red())
            emb.add_field( name = f'{member.name}', value = 'Отобран!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions( administrator = True )            
async def unadministrator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Админ')
            await member.remove_roles(mlmoderator)
            emb = discord.Embed(title = 'Администратор:', color = discord.Color.red())
            emb.add_field( name = f'{member.name}', value = 'Отобран!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions( administrator = True )            
async def ungladministrator(ctx, member: discord.Member):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            mlmoderator = discord.utils.get(ctx.message.guild.roles, name = 'Главный Админ')
            await member.remove_roles(mlmoderator)
            emb = discord.Embed(title = 'Главный Администратор:', color = discord.Color.red())
            emb.add_field( name = f'{member.name}', value = 'Отобран!')

            url1 = str(member.avatar_url)[:-10]
            
            emb.set_thumbnail(url = url1)
            emb.set_footer(text = f'ID: {member.id}')
            emb.set_author(name = f'Администратор: {ctx.author.name}')
            await ctx.send(embed = emb)
##############################################################################################################################

@bot.command()
async def повтори(ctx):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            if ctx.message.reference and (msg := ctx.message.reference.resolved) and isinstance(msg, discord.Message):
                await ctx.send(msg.content)
            else:
                await ctx.send("Ответь на сообщение.")


@bot.command()
async def профиль(ctx,member:discord.Member = None, guild: discord.Guild = None):
    await ctx.message.delete()
    if member == None:
        emb = discord.Embed(title="Информация:", color=ctx.message.author.color)
        emb.add_field(name="Name:", value=ctx.message.author.display_name,inline=False)
        emb.add_field(name="ID:", value=ctx.message.author.id,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роль:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=ctx.message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
    else:
        emb = discord.Embed(title="Информация:", color=member.color)
        emb.add_field(name="Name:", value=member.display_name,inline=False)
        emb.add_field(name="ID:", value=member.id,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = "⚪ Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Активность:", value=d,inline=False)
        emb.add_field(name="Статус:", value=member.activity,inline=False)
        emb.add_field(name="Роль:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Акаунт был создан:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),inline=False)
        await ctx.send(embed = emb)


@bot.command(pass_context = True)
async def help(ctx):
        cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
        if cursor.fetchone():#Если существует
            return
        else: 
            cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
            if cursor.fetchone()==None:#Если не существует
                return
            else:
                await ctx.channel.purge(limit = 1)
                emb = discord.Embed(title = 'Навигация', color = discord.Color.purple())

                emb.add_field( name = '_help', value = 'Посмотреть перечень команд')
                emb.add_field( name = '_аккаунт', value = 'Твой уровень сервера')
                emb.add_field( name = '_mute', value = 'Замьютить человека')
                emb.add_field( name = '_un_mute', value = 'Размьютить человека')
                emb.add_field( name = '_подтверждение', value = 'Информация о подтверждении номера')
                emb.add_field( name = '_номер +свойномер', value = 'Подтвердить номер телефона')
                emb.add_field( name = '_роль', value = 'Получить роль после подтверждения')
                emb.add_field( name = '_сайт', value = 'Наш официальный сайт')
                emb.add_field( name = '_карта', value = 'Получить свою карту сервера')
                emb.add_field( name = '_киквойс', value = 'Кикнуть человека с войс канала')
                emb.add_field( name = '_сервера', value = 'Секретная команда')
                emb.add_field( name = '_купить', value = 'Посмотреть цену на ботов')
                emb.add_field( name = '_покупатели', value = 'Кто последний купил бота')
                emb.add_field( name = '_clear', value = 'Очистить чат')
                emb.add_field( name = '_addserverB, D', value = 'Занести сервер в базу данных (для особых людей)')
                emb.add_field( name = '_blacklistB, D', value = 'Занести участника в блэк лист (для особых людей)')
                emb.add_field( name = '_mlmoderator', value = 'Выдать Младшего Модератора')
                emb.add_field( name = '_moderator', value = 'Выдать Модератора')
                emb.add_field( name = '_adminisrator', value = 'Выдать Администратора')
                emb.add_field( name = '_gladminisrator', value = 'Выдать Главного Администратора')
                emb.add_field( name = '_unmlmoderator', value = 'Отобрать Младшего Модератора')
                emb.add_field( name = '_unmoderator', value = 'Отобрать Модератора')
                emb.add_field( name = '_unadminisrator', value = 'Отобрать Администратора')
                emb.add_field( name = '_ungladminisrator', value = 'Отобрать Главного Администратора')
                emb.add_field( name = 'Посмотреть все команды:', value = '№№№№№№№№№№№№№№№№№№№№№№№№№№№№№')
                emb.set_thumbnail(url = 'https://i.ibb.co/8cD6Z0n/ece71c6d2eba5ee46e3246419882d86a-1.png')

                await ctx.send(embed = emb)


@bot.command(pass_context = True)
async def clear(ctx, amount = 500):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = amount)


@bot.event
async def on_member_remove(member, ctx):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            for ch in bot.get_guild(member.guild.id).channels:
                if ch.name == '👋〡приветствие':
                    await bot.get_channel(ch.id).send(f'Ну и вали >:( {member}')


@bot.command()
async def роль(ctx):
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
             cursor.execute(f"SELECT id FROM phone where id={ctx.author.id}")
             if cursor.fetchone()==None:#Если не существует
                 await ctx.send('С начало зарегестрируйте свой номер телефона по команде: _номер (свой номер)!')
             else:
                 await ctx.channel.purge(limit = 1)

                 role = discord.utils.get(ctx.message.guild.roles, name = 'Участник')
                 rmfole = discord.utils.get(ctx.message.guild.roles, name = 'Верифицирован')
                 await ctx.author.add_roles(role)
                 await ctx.author.remove_roles(rmfole)
                 emb = discord.Embed(title = 'Роль')
                 emb.add_field( name = f'{ctx.author.name}', value = '**Роль успешно выдана, наслаждайтесь пробыванием на сервере!**')
                 await ctx.send(embed = emb)                


def send_email(message):
    sender = "mydiscorddbinoneclick@mail.ru"
    # your password = "your password"
    password = "FWDYnzhruaI0Skot0Vv2"

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, f"Subject: NEW REGISTRATION USER\n{message}")

        return "The message was sent successfully!"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password please!"


@bot.command()
@commands.dm_only()
async def number(ctx, *, response):
    cursor.execute(f"SELECT id FROM phone where id={ctx.author.id}")
    if len(response) < 11 or len(response) > 15:
        await ctx.send('Такого телефонного номера не существует, вы были замучены на сервере!')
        await timeout_user(user_id=member.id, guild_id=ctx.guild.id, until=2880)
    else:
        if cursor.fetchone()==None:#Если не существует
             cursor.execute(f"INSERT INTO phone VALUES ({ctx.author.id}, '{ctx.message.author.name}', '{response}')")
             await ctx.send('Спасибо за честность, модераторы проверят ваши данные! Дальше направляйтесь на сервер в чат роль и вставте команду _роль')
             owner = bot.get_user(727450233449218108)
             user = (f'@{ctx.author.name}, ID: {ctx.author.id}, - {response}')
             await owner.send(f'{ctx.author.name}, ID: {ctx.author.id}, - {response}')
        else:#Если существует
             await ctx.send('Вы уже зарегестрированный пользователь, напишите модераторам чтобы они решили проблему со второй регистрацией!')
             pass
        conn.commit()


if __name__ == "__number__":
    number()

@bot.command()
async def аккаунт(ctx): #команда _account (где "_", ваш префикс указаный в начале)
    cursor.execute(f"SELECT id FROM blacklist where id={ctx.author.id}")#существует ли сервер в БД
    if cursor.fetchone():#Если существует
            return
    else: 
        cursor.execute(f"SELECT id FROM servers where id={ctx.guild.id}")#существует ли сервер в БД
        if cursor.fetchone()==None:#Если не существует
            return
        else:
            await ctx.channel.purge(limit = 1)
            table=[["nickname","lvl","xp","money"]]
            for row in cursor.execute(f"SELECT nickname,lvl,xp,money FROM users where id={ctx.author.id}"):
                table.append([row[0],row[1],row[2],row[3]])

            img = Image.new('RGBA', (390, 130), '#050514')
            url = str(ctx.author.avatar_url)[:-10]

            response = requests.get(url, stream = True)

            if not response:
                await ctx.send(f'{ctx.author.name} Тебе придется поставить аватарку, дружочек!')
                return
            else:
                response = Image.open(io.BytesIO(response.content))
            response = response.convert('RGBA')
            response = response.resize((100, 100), Image.ANTIALIAS)

            img.paste(response, (15, 15, 115, 115))

            idraw = ImageDraw.Draw(img)
            name = ctx.author.name
            tag = ctx.author.discriminator

            headline = ImageFont.truetype('days2.ttf', size = 20)
            undertext = ImageFont.truetype('KarloCham-Line.otf', size = 18)
            ps = ImageFont.truetype('KarloCham-Line.otf', size = 18)
            headline2 = ImageFont.truetype('days2.ttf', size = 10)
            headline3 = ImageFont.truetype('days2.ttf', size = 10)
            headline4 = ImageFont.truetype('KarloCham-Line.otf', size = 18)

            idraw.text((145, 5), f'{name}#{tag}', font = headline)
            idraw.text((145, 35), f'Money - {row[3]}', font = headline4)
            idraw.text((145, 55), f'lvl - {row[1]}', font = undertext)
            idraw.text((145, 75), f'Xp - {row[2]}', font = ps)
            idraw.text((145, 105), f'ID: {ctx.author.id}', font = headline2)
            idraw.text((375, 10), '. .\nA\nR\nA\nM\nI\nR\nA', '#ffff56', font = headline3)

            img.save('akaunt_card.png')

            await ctx.send(file = discord.File(fp = 'akaunt_card.png'))


    conn.commit()#применение изменений в БД


# Реклама 100 участников = 30 руб(на нашем сервере)

# @bot.command()
# async def jlby(ctx):
#      await ctx.channel.purge(limit = 1)
#      emb = discord.Embed(title = 'Дискорд сервер Арамира', color = discord.Color.red())
#      emb.add_field( name = 'Описание:', value = 'Хороший дискорд сервер где можно по чилить, хорошо провести время , пообщаться с умными людьми и получить карточку!')
#      emb.set_thumbnail(url = 'https://i.ibb.co/yhq4NNJ/7055fb23a39b38ca42446f3596ca3591.png')
#      emb.set_footer(text = 'ID: 835650277515460609')
#      emb.add_field( name = '📎〡Ссылка Приглашения:', value = 'https://discord.gg/zyD5DCPx')
#      emb.add_field( name = 'Участников:', value = '14 👤')
#      emb.set_author(name = 'Владелец: dextrey')
#      await ctx.send(embed = emb)




@bot.event
async def on_member_join(member):
    cursor.execute(f"SELECT id FROM users where id={member.id}")#все также, существует ли участник в БД
    if cursor.fetchone()==None:#Если не существует
        cursor.execute(f"INSERT INTO users VALUES ({member.id}, '{member.name}', '<@{member.id}>', 50000, 'S','[]',1,1)")#вводит все данные об участнике в БД
        channel = bot.get_channel(908371587621867540)
        await channel.send(f'У нас новый участник - {member.name}#{member.discriminator}, ID: {member.id}, Добро пожаловать:)')
    else:#Если существует
        pass
    conn.commit()#применение изменений в БД

@bot.event
async def on_message(message):
    if len(message.content) > 30:#за каждое сообщение длиной > 10 символов...
        for row in cursor.execute(f"SELECT xp,lvl FROM users where id={message.author.id}"):
            expi=row[0]+random.randint(5, 40)#к опыту добавляется случайное число
            cursor.execute(f'UPDATE users SET xp={expi} where id={message.author.id}')
            lvch=expi/(row[1]*1)
            print(int(lvch))
            lv=int(lvch)
            if row[1] < lv:#если текущий уровень меньше уровня, который был рассчитан формулой выше,...
                await message.channel.send(f'Новый уровень!')#то появляется уведомление...
                bal=1*lv
                cursor.execute(f'UPDATE users SET lvl={lv} where id={message.author.id}')#и участник получает деньги
    await bot.process_commands(message)#Далее это будет необходимо для ctx команд
    conn.commit()#применение изменений в БД

with open('.env', 'r') as file:
    line = file.readline()
    try:
        os.environ[line[:line.find("=")]]=line[line.find("=")+1:]
    except ValueError:
        pass

bot.run()
