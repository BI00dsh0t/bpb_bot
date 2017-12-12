from discord.ext import commands

d = "Basic bot to keep the pins cleans... cuz nigga I'm bored"

bot = commands.Bot(command_prefix='!')

pinups_str = 'pinups'


@bot.command()
async def recycle(num: int):
    channel = bot.get_channel('227549008711778305')
    pins = await bot.pins_from(channel)
    messages = list(pins)

    count = 0

    for message in messages:
        if len(message.content) > 0:
            await bot.say(message.content)
        if len(message.attachments) > 0:
            await bot.say(message.attachments[0].get('url'))

        count = count + 1

        if count >= num:
            break
    return


async def purge(message):
    if message.content.startswith('!purge'):
        num = int(message.content.split(' ')[1])
        await bot.purge_from(channel=message.channel, limit=num, before=message)
    return


@bot.command()
async def description():
    await bot.say(d)
    return


bot.add_listener(purge, 'on_message')

bot.run('Mzg5NjE1Nzg0OTgyMzQ3Nzgw.DRBzpQ.uLqhIxgA9q0a1C55xzn2GUDZcFQ')
