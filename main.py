import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def rolldice(ctx):
    dice = random.randint(1,6)
    await ctx.send(f"Выпало число {dice}")

@bot.command()
async def mywife(ctx):
    users = ctx.guild.members
    user2 = random.choice(users)
    await ctx.send(f"Жена {ctx.author.name}, - {user2}")

@bot.command()
async def amicool(ctx):
    cool = random.choice([
        'Нет, ты лох',
        'Да, ты лучший человек',
        'Нет, ты неудачник',
        'Да, я думаю что ты хороший друг'
    ])
    await ctx.send(cool)

@bot.command()
async def myhusband(ctx):
    users = ctx.guild.members
    user2 = random.choice(users)
    await ctx.send(f"Муж {ctx.author.name}, - {user2}")

@bot.command()
async def pet(ctx):
    users = ctx.guild.members
    user = random.choice(users)
    await ctx.send(f"{ctx.author.name} погладил {user}")

@bot.command()
async def TorA(ctx):
    true = [
        'Первая любовь',
        "Куришь ли?",
        "Ты зависим от соц сетей?",
        "Расскажи про то, за что тебе стыдно",
        "Расскажи про хобби",
        "Если бы ты мог делать всё что угодно, чтобы ты сделал в первую очередь?"
    ]

    action = [
        'Спой в голосовом канале любую песню на английском (другом языке кроме русского)',
        'Сними на камеру, как ты падаешь со стула',
        "Сделай интерпритатор",
        'В прямом эфире, напиши "Hello World!" на десяти разных языках (программирования)'
    ]

    randomnum = random.randint(1,2)
    if randomnum == 1:
        message = random.choice(true)
    elif randomnum == 2:
        message = random.choice(action)
    await ctx.send(message)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def help(ctx):
    message = "'>rolldice'-кинуть кубик\n'>mywife' - узнать жену\n'>myhusband' - узнать мужа\n'>amicool' - бот скажет кто ты\n'>pet' - погладить\n'>TorA' - правда или действие\n'>meme' - отправляет рандомный мем"
    await ctx.send(message)

bot.run("token")
