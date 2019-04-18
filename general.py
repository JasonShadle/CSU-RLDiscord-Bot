def deleteMessage(message, time=None):
    if time==None:
        client.delete_message()
