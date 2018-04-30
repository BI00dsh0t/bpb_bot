import os

from discord.ext import commands

d = "Basic bot to keep the pins cleans... cuz dawg I'm bored"

bot = commands.Bot(command_prefix='!')


# red = redis.from_url(os.environ.get("REDIS_URL"))


@bot.command()
async def recycle(num: int):
    channel = bot.get_channel('227549008711778305')
    pins = await bot.pins_from(channel)
    messages = list(pins)
    pinups_channel = bot.get_channel('389590243336126466')

    count = 0

    for message in messages:
        if len(message.content) > 0:
            await bot.send_message(pinups_channel, message.content)
        if len(message.attachments) > 0:
            await bot.send_message(pinups_channel, message.attachments[0].get('url'))

        count = count + 1

        await bot.unpin_message(message)

        if count >= num:
            break
    return


async def purge(message):

    if message.content.startswith('!purgeme'.lower()):
        num = int(message.content.split(' ')[1])

        counter = 0

        while counter < num:
            messages = bot.logs_from(message.channel, 100, message)

            for mes in messages:
                if mes.author == message.author:
                    bot.delete_message(mes)
                    counter += 1

    elif message.content.startswith('!purge'.lower()):
        num = int(message.content.split(' ')[1])
        await bot.purge_from(channel=message.channel, limit=num, before=message)
        
    return


@bot.command()
async def help():
    await bot.say('Please use !help <command> for further explanation of each command')


async def blood(message):
    if 'bloodshot problem' in message.content or 'bloodshot issue' in message.content:
        await bot.send_message(message.channel, 'leave blood alone <:lirikThump:311191142286884864>')


@bot.command()
async def description():
    await bot.say(d)
    return


bot.add_listener(purge, 'on_message')
bot.add_listener(blood, 'on_message')

bot.run(os.environ.get('bot_code'))
