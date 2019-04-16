def deleteMessage(message, client, time=None):
    if time==None:
        client.delete_message()
