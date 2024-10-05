# Задача "Рассылка писем"
def send_email(message, recipient, sender = "university.help@gmail.com"):
    domens = (".com", ".ru", ".net") # строка или картеж суфиксов для проверки методом .endswith()
    if '@' in recipient and '@' in sender:
        if recipient.lower().endswith(domens) and sender.lower().endswith(domens):
            if recipient == sender:
                print("Нельзя отправить письмо самому себе!")
            elif sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
             print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    print(message)


print(send_email('Hellow, I am fogetful', 'rokabc.com'))
print(send_email('Hellow, I am fogetful', 'rok@abc.cm'))
print(send_email('Everything all right', 'rok@abc.com', "help@gmail.com"))
print(send_email('You are credited', 'rok@abc.com'))
print(send_email('A note to youself', "university.help@gmail.com", "university.help@gmail.com"))
