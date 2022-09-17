import json
import typing
import asyncio
import links

with open("info.json", encoding='utf-8') as meu_json:
    Token = json.load(meu_json)

import discord
import random
from itertools import cycle
from discord.ext import commands, tasks

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
status = cycle(['Izidio da janela', 'Flappy Izidio', 'Animalia', 'Izidio Shooter', 'Minecraft Jukebox', '-se de um prédio', 'Izidio e o balão'])

emot = '💚'
msg_id = None
msg_user = None

@bot.event
async def on_ready():
    change_S.start()
    print("Estou pronto! Conectado como {0.user}".format(bot))

bot.remove_command("help")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Comando inválido, jamanta!")
    if isinstance(error, commands.UserNotFound):
        await ctx.send("Use-me direito, mortal!")

@bot.command(name="hello")
async def send_hello(ctx):
    name = ctx.author.name
    await ctx.send("Olá, " + name + ". Como está a sua vida patética?")

@bot.command(name="ajuda")
async def dm(ctx):
    await ctx.author.send("Quem ousa retirar-me de meu descanso?")

@bot.event
async def on_member_join(member):
    await member.send(f'Olá, mortal {member.name}. Bem vindo ao servidor!')

@bot.command(name="cargo")
async def cargo(ctx):

    embed = discord.Embed(
        title = "Olá, pegue o cargo!",
        color = 0x057248,
        description = "Mashairos = 💚\n"
    )

    embed.set_author(name='Lagostinho',
    icon_url='https://cdn-icons-png.flaticon.com/512/468/468392.png')
    botmsg = await ctx.send(embed=embed)
    await botmsg.add_reaction(emoji=emot)

    global msg_id
    msg_id = botmsg.id

@bot.command(name="say")
async def say(ctx, *, question):
    await ctx.message.delete()
    await ctx.send(f'{question}')

@bot.command(name="clear")
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount+1)


@bot.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "💚" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Shashairos", msg.guild.roles)
        await user.add_roles(role)

@bot.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "💚" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Shashairos", msg.guild.roles)
        await user.remove_roles(role)

@bot.command(name="roll", aliases=["r", "d"])
async def dado(ctx, x:int, y:typing.Optional[int]= None, op:typing.Optional[str]= None, z:typing.Optional[int]= None):
    dados = []

    if y is None:
        y = x
        x = 1 

    f = 0
    while f < x: 
        dados.append(random.randint(1,y))
        f += 1
    SumZ = sum(dados)

    if op == "-":
        SumZ = sum(dados)-z
        await ctx.reply(f'Resultado: {SumZ} {dados}-{z}')
    if op == "+":
        SumZ = sum(dados)+z
        await ctx.reply(f'Resultado: {SumZ} {dados}+{z}')
    if op is None:
        await ctx.reply(f'Resultado: {SumZ} {dados}')

@bot.command(name="punch")
async def punch(ctx, x: discord.Member):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} bateu em você {x.mention}')  
        embed.set_author(name=f'{x.guild.name}')
        embed.set_image(url=(random.choice(links.punch_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def kiss(ctx, x: discord.Member):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} beijou você {x.mention}')  
        embed.set_author(name=f'{x.guild.name}')
        embed.set_image(url=(random.choice(links.kiss_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def hug(ctx, x: discord.Member):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} abraçou você {x.mention}')  
        embed.set_author(name=f'{x.guild.name}')
        embed.set_image(url=(random.choice(links.hug_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def lick(ctx, x: discord.Member):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} lambeu você {x.mention}')  
        embed.set_author(name=f'{x.guild.name}')
        embed.set_image(url=(random.choice(links.lick_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def bite(ctx, x: discord.Member):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} mordeu você {x.mention}')  
        embed.set_author(name=f'{x.guild.name}')
        embed.set_image(url=(random.choice(links.bite_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def pat(ctx, x: discord.Member):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} fez carinho em você {x.mention}')  
        embed.set_author(name=f'{x.guild.name}')
        embed.set_image(url=(random.choice(links.pat_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def lewd(ctx):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} está pensando em coisas pervertidas')  
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_image(url=(random.choice(links.lewd_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def blush(ctx):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} está envergonhado')  
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_image(url=(random.choice(links.blush_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def cry(ctx):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} está chorando')  
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_image(url=(random.choice(links.cry_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def angry(ctx):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} está com raiva')  
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_image(url=(random.choice(links.angry_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def happy(ctx):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} está feliz')  
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_image(url=(random.choice(links.happy_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def love(ctx):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'{ctx.author.mention} está amando')  
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_image(url=(random.choice(links.love_gifs)))
        await ctx.send(embed=embed)

@bot.command()
async def maid(ctx):
        embed = discord.Embed(color=(discord.Colour.random()), description=f'Maidzinha ao seu dispor!')  
        embed.set_author(name=f'{ctx.guild.name}')
        embed.set_image(url=(random.choice(links.maid_gifs)))
        await ctx.send(embed=embed)

@bot.command(name='spam')
async def spam(ctx, member: discord.Member, amount:int, *, message):
    for i in range(amount):
        await asyncio.sleep(1)
        await member.send(message)
    
@bot.command(name='spiderS')
async def spiderS(ctx, member: discord.Member, amount:int):
    embed = discord.Embed(title="...", description=f'Aranhinha >;3') 
    for i in range(amount):
        await asyncio.sleep(1)
        embed.set_image(url=(random.choice(links.spider_gifs)))
        await member.send(embed=embed)

@tasks.loop(seconds=180)
async def change_S():
    await bot.change_presence(activity=discord.Game(next(status)))

bot.run(Token["TOKEN"])