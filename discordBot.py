import discord
from discord.ext import commands
import foodpanda
from datetime import datetime, timezone, timedelta
import gc

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user} ready on!!!')


@bot.command(name='eat')
async def eat(ctx):
    name, tag, star, category, time, fee, img = foodpanda.eatWhat()
    embed = discord.Embed(title=name, color=discord.Color.random(), url=tag,
                          timestamp=datetime.now(timezone(timedelta(hours=+8))))
    embed.add_field(name='評價', value='\u2606'+star, inline=True)
    embed.add_field(name='類型', value=category, inline=True)
    embed.add_field(name='', value='', inline=True)
    embed.add_field(name='外送時間', value=time, inline=True)
    embed.add_field(name='外送費', value=fee, inline=True)
    embed.add_field(name='', value='', inline=True)
    embed.set_image(url=img)
    embed.set_footer(text='僅供虎科大地區使用')
    await ctx.reply(embed=embed)
    del (name, tag, star, category, time, fee, img)
    gc.collect()
    print(f'reply a request from {ctx.author} in {ctx.channel}')

bot.run('MTIxMDE1NDY3MTMxOTE1NDcyOQ.GPe71v.rcsl42x3sNYSnHcfBxIyDGHXalwpOsKJw0cTZo')
