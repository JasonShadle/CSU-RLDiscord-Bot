import discord, config
from roles import Roles
class MyClient(discord.Client):
    # preset admins with Discord ID's
    adminList = ['106876197698355200']

    # on bot startup
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

#    async def on_member_join(self, member):

    # when a message is sent
    async def on_message(self, message):

        # set some default variables to make it easier
        id = message.author.id
        content = message.content

        # check admin list + server admin privilege 
        if id in MyClient.adminList or message.author.guild_permissions.administrator:
            admin = True
        else:
            admin = False

        if content == '!ping':
            await message.channel.send(message.author.mention + ': Pong!')
            
        elif content == '!admin':
            if admin:
                await message.channel.send(message.author.mention + ': You are an admin')
            else:
                await message.channel.send(message.author.mention + ': You are not an admin')
        elif content[:6] == '!role ':
            r = Roles(message, client)
            if (r.getError() == True):
                await message.channel.send(message.author.mention + ': That role can\'t be assigned')
            else:
                if (r.getHasRole()):
                    await message.author.remove_roles(r.getRole())
                    await message.channel.send(message.author.mention + ': Role `'+ r.getRole().name + '` has been removed.')
                else:
                    await message.author.add_roles(r.getRole())
                    await message.channel.send(message.author.mention + ': Role `'+ r.getRole().name + '` has been added.')

client = MyClient()
client.run(config.clienttoken)
