import asyncio

async def deleteTimedMessage(time, *messages):
	await asyncio.sleep(time)
	for message in messages:
		await message.delete(message)
	