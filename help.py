import discord

async def help(message):
    embed = discord.Embed(color=0x006341, title='Commands:', inline=False)
    embed.add_field(name='!roles', value='Display the available roles to assign', inline=False)
    embed.add_field(name='!roles [rolename]', value='Assign yourself the role', inline=False)
    embed.add_field(name='Issues?', value='Message CakeRaider#3607 for help', inline=False)
    await message.channel.send(message.author.mention + ':', embed=embed)