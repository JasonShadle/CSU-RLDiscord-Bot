import asyncio

async def deleteTimedMessage(message, time):
	await asyncio.sleep(time)
	await message.delete()
	