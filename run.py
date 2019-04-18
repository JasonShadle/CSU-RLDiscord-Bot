import discord, config, asyncio
from roles import Roles
from general import deleteTimedMessage

adminList = config.adminList

class MyClient(discord.Client):
    # preset admins with Discord ID's


    # on bot startup
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

#    async def on_member_join(self, member):

    # when a message is sent
    async def on_message(self, message):
        print('Message in {0.channel.name} from {0.author}: {0.content}'.format(message))
        # set some default variables to make it easier
        id = message.author.id
        content = message.content
        channelName = message.channel.name

        # check admin list + server admin privilege 
        if id in adminList or message.author.guild_permissions.administrator:
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
        elif content[:7] == '!roles ':
            if channelName in ('role-request', 'only-me','bot-setup-and-repair') :
                if content[7:11] == 'list':
                    embed = discord.Embed()
                    with open(config.rolesFile, 'r') as file:
                        roleLine = ''
                        for line in file:
                            roleLine += '\n' + line
                        embed.add_field(name='Self-Assigned Roles List', value = roleLine)
                if content[7:14] == 'toggle ':
                    if admin:
                        r = Roles(message)
                        roleName = content[13:].lower()
                        if r.toggle(roleName):
                            botMessage = await message.channel.send('{0}: Role `{1}` has been deleted'.format(message.author.mention, roleName))
                            await asyncio.sleep(3)                         
                            await message.delete()                         
                            await botMessage.delete()
                            
                        else:
                            await message.channel.send('{0}: Role `{1}` has been added'.format(message.author.mention, roleName))

            else:
                r = Roles(message)
                if (r.getError()):
                    botMessage = await message.channel.send(message.author.mention + ': That role can\'t be assigned')
                    await asyncio.sleep(3)                         
                    await message.delete()                        
                    await botMessage.delete()

                else:
                    if (r.getHasRole()):
                        await message.author.remove_roles(r.getRole())
                        botMessage = await message.channel.send(message.author.mention + ': Role `'+ r.getRole().name + '` has been removed.')
                        await asyncio.sleep(3)
                        await message.delete()
                        await botMessage.delete()

                    else:
                        await message.author.add_roles(r.getRole())
                        botMessage = await message.channel.send(message.author.mention + ': Role `'+ r.getRole().name + '` has been added.')
                        await asyncio.sleep(3)
                        await message.delete()
                        await botMessage.delete()
        elif content == '!roles list':
            embed = discord.Embed()
            with open(config.rolesFile, 'r') as file:
                roleLine = ''
                for line in file:
                    roleLine += '\n' + line
                embed.add_field(name='Self-Assigned Roles List', value = roleLine)
            await message.channel.send(message.author.mention, embed=embed)
client = MyClient()
client.run(config.clienttoken)
