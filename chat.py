#!/usr/bin/python
# -*- coding NAIVY PROD -*-
#-*- coding RUX -*-
# Author: https://vk.com/naivy1

import vk, urllib.request, urllib.error, urllib.parse, json, random, time

print('╔══╗─╔╗╔╗─╔══╗─╔════╗───╔══╗─╔═══╗─╔══╗─╔╗──╔╗')
print('║╔═╝─║║║║─║╔╗║─╚═╗╔═╝───║╔═╝─║╔═╗║─║╔╗║─║║──║║')
print('║║───║╚╝║─║╚╝║───║║─────║╚═╗─║╚═╝║─║╚╝║─║╚╗╔╝║')
print('║║───║╔╗║─║╔╗║───║║─────╚═╗║─║╔══╝─║╔╗║─║╔╗╔╗║')
print('║╚═╗─║║║║─║║║║───║║─────╔═╝║─║║────║║║║─║║╚╝║║')
print('╚══╝─╚╝╚╝─╚╝╚╝───╚╝─────╚══╝─╚╝────╚╝╚╝─╚╝──╚╝')
print('                   V 1.0                       ')
print('                 By NAIVY PROD                 ')
config = {}

try:
	exec(compile(open("config.py", "rb").read(), "config.py", 'exec'), config)
except IOError:
	print("Не удалось получить логин и пароль, Введите их снова с помощью: python auth.py")
	input('нажмите ENTER для выхода') 


url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'], config['password'])

try:
    r = urllib.request.urlopen(url)
except urllib.error.HTTPError:
    print("Неверный логин или пароль (Перезапишите c помошью python auth.exe)")
    input('нажмите ENTER для выхода')

r = r.read()
token = json.loads(r)["access_token"] 
session = vk.Session(access_token = token)
vk = vk.API(session)

try:
    cs = open('chat-spam.txt', 'r', encoding='utf-8').read().splitlines()
except IOError:
    open('chat-spam.txt', 'w', encoding='utf-8')
    print("Словарь спама отсутствует. Был создан новый chat-spam.txt")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

if not cs:
    print("Словарь спама пуст. Добавьте в него слова.")
    print("!!!Предупреждение!!!")
    print("Каждое новую реплику писать через Enter")
    input('нажмите ENTER для выхода')
    exit(1)

print("Словарь спама:")
print()
print()
print (cs)
print()
print()
victim = input("id группы: ")

r = vk.users.get(user_ids = victim, fields = "id", v = 5.73)
r = r[0]["id"]

victim = r
print("Спам запущен")
print()
print("Нажмите Ctrl+C для выхода")
def mainloop():
    while(1):
        time.sleep(7)
        r = vk.messages.send(peer_id =2000000000 + victim, message = random.choice(cs), v = 5.73)
        print()
        print("Жди...")
        time.sleep(20)
        print("Отправлено:  ",random.choice(cs))
        pass

mainloop()
