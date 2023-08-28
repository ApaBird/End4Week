from ClearMessage import isBanWord, clearBanWord

message = input("Введите текст: ")

if isBanWord(message):
   message = clearBanWord(message)

with open("message.txt", 'a') as file:
    file.write(message)