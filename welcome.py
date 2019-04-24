import discord

async def welcome(user):
    presidentID = '166358373879644161'
    introChannelID = '534895896895422474'
    roleReqChannelID = '553456731225587724'
    rocketChannelID = '548656685603094528'
    message = '**Welcome to the CSU Rocket League Discord!**\n\n**If you go to CSU:**\n1. Go to https://orgsync.com/178859/chapter '\
        'and join with password `rocketleaguecsu`\n\n2. Message <@{0}> so you can sign a waiver (required by all sports clubs\n\n'\
        '3. Also let <@{0}> know if you plan on trying out for the competitive team (1st or 2nd team)\n\n'\
        '**For everyone:**\n\n1. Head to the <#{1}> channel to get to know everyone and for them to get to know you\n\n'\
        '2. Post your Rocket ID in the <#{2}> channel\n\n'\
        '3. Head over to <#{3}> channel to get your role'.format(presidentID, introChannelID, roleReqChannelID, rocketChannelID)
    
    await user.send(message)

# async def welcome(user):
#     presidentID = '166358373879644161'
#     introChannelID = '534895896895422474'
#     roleReqChannelID = '553456731225587724'
#     rocketChannelID = '548656685603094528'
#     message = '**Welcome to the CSU Rocket League Discord!**\n\n**If you go to CSU:**\n1. Go to [OrgSync](https://orgsync.com/178859/chapter) '\
#         'and join with password `rocketleaguecsu`\n\n2. Message <@{0}> so you can sign a waiver (required by all sports clubs\n\n'\
#         '3. Also let <@{0}> know if you plan on trying out for the competitive team (1st or 2nd team)\n\n'\
#         '**For everyone:**\n\n1. Head to the <#{1}> channel to get to know everyone and for them to get to know you\n\n'\
#         '2. Post your Rocket ID in the <#{2}> channel\n\n'\
#         '3. Head over to <#{3}> channel to get your role'.format(presidentID, introChannelID, roleReqChannelID, rocketChannelID)
    
#     await user.send(message)