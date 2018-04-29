import os

from discord.ext import commands

d = "Basic bot to keep the pins cleans... cuz dawg I'm bored"

bot = commands.Bot(command_prefix='!')

#red = redis.from_url(os.environ.get("REDIS_URL"))


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

        await bot.unpin_message(message)

        if count >= num:
            break
    return


async def purge(message):
    if message.content.startswith('!purge'.lower()):
        num = int(message.content.split(' ')[1])
        await bot.purge_from(channel=message.channel, limit=num, before=message)

    elif message.content.startswith('!purgeme'.lower()):
        num = int(message.content.split(' ')[1])

        counter = 0

        while counter < num:
            messages = bot.logs_from(message.channel, 100, message)

            for mes in messages:
                if mes.author == message.author:
                    bot.delete_message(mes)
                    counter += 1
    return


@bot.command()
async def description():
    await bot.say(d)
    return


bot.add_listener(purge, 'on_message')


bot.run(os.environ.get('bot_code'))
