def send_email(message, recepient, sender="university.help@gmail.com"):
  stop = 0                                            # контролька на корректность адреса почты
  if "@" not in recepient:                            # проверка на @ у получателя
      # print("@ нет в адресе" + "\n")
      stop += 1
  else:
      if ".com" in recepient:                         # проверка на .com в адресе
          # print(".com в адресе" + "\n")
          stop = stop                                 # если все ок, то stop = текущему значению stop
      elif ".ru" in recepient:                        # проверка на .ru в адресе
          # print(".ru в адресе" + "\n")
          stop = stop                                 # если все ок, то stop = текущему значению stop
      elif ".net" in recepient:                       # проверка на .net в адресе
          # print(".net в адресе" + "\n")
          stop = stop                                 # если все ок, то stop = текущему значению stop
      else:
          # print(recepient, "ни одного домена не указано" + "\n")
          stop += 1                                   # если ни одного домена не указано, то stop = stop + 1

  if "@" not in sender:                               # проверка на @ у отправителя
      # print("@ нет в адресе" + "\n")
      stop += 1
  else:
      if ".com" in sender:                             # проверка на .com в адресе
          # print(".com в адресе" + "\n")
          stop = stop
      elif ".ru" in sender:                            # проверка на .ru в адресе
          # print(".ru в адресе" + "\n")
          stop = stop
      elif ".net" in sender:                           # проверка на .net в адресе
          # print(".net в адресе" + "\n")
          stop = stop
      else:
          # print(sender, "ни одного домена не указано" + "\n")
          stop += 1

  if stop != 0:                                        # если stop не равен 0, то выводим сообщение об ошиб
      print("Невозможно отправить письмо  с адреса: ", sender, end="")
      print("на адрес: ", recepient + "\n")
      return                                           
  else:
      # print("адреса корректны!" + "\n")
      pass
  # print(message, recepient, sender)

  if recepient == sender:                               # если отправитель и получатель одинаковые, то
      print("Нельзя отправить письмо самому себе!" + "\n")
  else:                                                 # иначе
      if sender != "university.help@gmail.com":
          print("\nНЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: ", end="")
          print(sender, "на адрес: ", recepient + "\n")
      else:
          print("\nПисьмо успешно отправлено с адреса: ", sender, "на адрес: ", recepient + "\n")
###########################################################################################################

# ПРОИЗВОЛЬНЫЕ значения
send_email("Сёма привет!", "university.help@gmail.com")
print("#" * 50)
send_email("Сёма привет!", "abricos@gmail.net")
print("#" * 50)
send_email("Сёма привет!", "abricos@gmail.net", "aicos@gmail.net")
print("#" * 50)

for i in range(6):
  print()

# Значения по ДЗ
print("Условия по Домашнему заданию:" + "\n ")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
