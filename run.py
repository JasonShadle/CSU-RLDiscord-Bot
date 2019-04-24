import discord, config, asyncio
from roles import Roles
from general import deleteTimedMessage
from help import help
from welcome import welcome

adminList = config.adminList

class MyClient(discord.Client):
    # preset admins with Discord ID's


    # on bot startup
    async def on_ready(self):
        print('Logged on as {0}'.format(self.user))

    async def on_member_join(self, member):
        await welcome(member)
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

        elif content == '!help':
            embed = discord.Embed(color=0x006341, title='Commands')
            await help(message)
            
        elif content == '!admin':
            if admin:
                await message.channel.send(message.author.mention + ': You are an admin')
            else:
                await message.channel.send(message.author.mention + ': You are not an admin')
        elif content[:7] == '!roles ':
            botMessage = ''
            if channelName in ('role-request'):
                if content[7:14] == 'toggle ':
                    if admin:
                        r = Roles(message)
                        roleName = content[14:].lower()
                        if r.toggle(roleName):
                            botMessage = await message.channel.send('{0}: Role `{1}` has been deleted'.format(message.author.mention, roleName))
                            # await deleteTimedMessage(10, [message, botMessage])
                            
                        else:
                            botMessage = await message.channel.send('{0}: Role `{1}` has been added'.format(message.author.mention, roleName))
                    # await deleteTimedMessage(10, [message, botMessage])

                else:
                    r = Roles(message)
                    if (r.getError()):
                        botMessage = await message.channel.send(message.author.mention + ': That role can\'t be assigned')

                    else:
                        if (r.getHasRole()):
                            await message.author.remove_roles(r.getRole())
                            botMessage = await message.channel.send(message.author.mention + ': Role `'+ r.getRole().name + '` has been removed.')

                        else:
                            await message.author.add_roles(r.getRole())
                            botMessage = await message.channel.send(message.author.mention + ': Role `'+ r.getRole().name + '` has been added.')
                
                    # await deleteTimedMessage(10, [message, botMessage])

        elif content == '!roles':
            embed = discord.Embed(color=0x006341, title='Self-Assigned Roles List:')
            with open(config.rolesFile, 'r') as file:
                for line in file:
                    name = line
                    value = '!roles ' + line
                    embed.add_field(name=name, value=value, inline=False)
        
            botMessage = await message.channel.send('{0}:'.format(message.author.mention), embed=embed)
            # await deleteTimedMessage(60, [message, botMessage])
        # elif content == '!logoff':
        #     if id in adminList:
        #         client.logoff()

client = MyClient()
client.run(config.clienttoken)
