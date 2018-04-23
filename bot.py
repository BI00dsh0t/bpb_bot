from discord.ext import commands
import discord
import os
import redis

d = "Basic bot to keep the pins cleans... cuz dawg I'm bored"

bot = commands.Bot(command_prefix='!')

red = redis.from_url(os.environ.get("REDIS_URL"))


@bot.command()
async def recycle(num: int):
    channel = bot.get_channel('227549008711778305')
    pins = await bot.pins_from(channel)
    messages = list(pins)

    count = 0

    for message in messages:
        if len(message.content) > 0:
            await bot.send_message('389590243336126466', message.content)
        if len(message.attachments) > 0:
            await bot.send_message('389590243336126466', message.attachments[0].get('url'))

        count = count + 1

        if count >= num:
            break
    return


async def purge(message):
    if message.content.startswith('!purge'):
        num = int(message.content.split(' ')[1])
        await bot.purge_from(channel=message.channel, limit=num, before=message)
    return


async def blood(message):
    if 'bloodshot problem' or 'bloodshot issue' in message.content:
        await bot.send_message(message.channel, 'leave blood alone <:lirikThump:311191142286884864>')
    return


async def jm_dab_count(message: discord.Message):
    if message.author.id == '171567323017117696' and '<:TatDab:255555983437332480>' in message.content:
        red.incr('dab')
        bot.send_message(message.channel, '{} has dabbed  {} times'.format(message.author.nick, red.get('dab')))
        red.bgsave()
    return


@bot.command()
async def description():
    await bot.say(d)
    return


bot.add_listener(purge, 'on_message')
bot.add_listener(blood, 'on_message')
bot.add_listener(jm_dab_count, 'on_message')

bot.run(os.environ.get('bot_code'))
