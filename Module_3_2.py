def send_email(message, recepient, sender="university.help@gmail.com"):
    stop = 0
    if "@" not in recepient:
        # print("@ нет в адресе" + "\n")
        stop += 1
    else:
        if ".com" in recepient:
            # print(".com в адресе" + "\n")
            stop = stop
        elif ".ru" in recepient:
            # print(".ru в адресе" + "\n")
            stop = stop
        elif ".net" in recepient:
            # print(".net в адресе" + "\n")
            stop = stop
        else:
            # print(recepient, "ни одного домена не указано" + "\n")
            stop += 1

    if "@" not in sender:
        # print("@ нет в адресе" + "\n")
        stop += 1
    else:
        if ".com" in sender:
            # print(".com в адресе" + "\n")
            stop = stop
        elif ".ru" in sender:
            # print(".ru в адресе" + "\n")
            stop = stop
        elif ".net" in sender:
            # print(".net в адресе" + "\n")
            stop = stop
        else:
            # print(sender, "ни одного домена не указано" + "\n")
            stop += 1

    if stop != 0:
        print("Невозможно отправить письмо  с адреса: ", sender, end="")
        print("на адрес: ", recepient + "\n")
        return
    else:
        # print("адреса корректны!" + "\n")
        pass
    # print(message, recepient, sender)

    if recepient == sender:
        print("Нельзя отправить письмо самому себе!" + "\n")
    else:
        if sender != "university.help@gmail.com":
            print("\nНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: ", end="")
            print(sender, "на адрес: ", recepient + "\n")
        else:
            print("\nПисьмо успешно отправлено с адреса: ", sender, "на адрес: ", recepient + "\n")
###########################################################################################################

send_email("Сёма привет!", "university.help@gmail.com")
print("#" * 50)
send_email("Сёма привет!", "abricos@gmail.net")
print("#" * 50)
send_email("Сёма привет!", "abricos@gmail.net", "aicos@gmail.net")
print("#" * 50)

for i in range(6):
    print()

print("Условия по Домашнему заданию:" + "\n ")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')