LISTBANWORD = ["лист", "облако"]


def clearBanWord(message):
    for word in LISTBANWORD:
        while word in message.lower():
            dot = message.lower().find(word)
            message = message[:dot] + '*' * len(word) + message[dot + len(word):]


def isBanWord(message):
    for word in LISTBANWORD:
        if word in message.lower():
            return True

    return False