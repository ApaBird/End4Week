from ClearMessage import isBanWord, clearBanWord

message = input("Введите текст: ")

if not isBanWord(message):
    print("Очистка текста.....")
    message = clearBanWord(message)

with open("message.txt", 'a') as file:
    file.write(message)

