import vk_api
import random
import config
import anek
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk = vk_api.VkApi(token=config.mytoken)
vk._auth_token()
vk.get_api()
longpoll = VkBotLongPoll(vk, config.myid)


def send_msg(peer_id: int, message: str, attachment: str = ""):
    return vk.method("messages.send", {**locals(), "random_id": 0})

while True:
    try:
       for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                   if event.object.peer_id != event.object.from_id: #конфа
                       roll= random.randint(1, 100)
                       if event.object.text == "/roll": #Случайное число от 1 до 100
                        (send_msg(event.obj.peer_id, "Ваше число - " + str(roll)) )
                       if event.object.text == "/joke": #Анекдот категории Б
                        (send_msg(event.obj.peer_id, "Ваш анекдот: \n" + str(joke) ))
                       if event.object.text == "/help": 
                        (send_msg(event.obj.peer_id, "Вот что я умею: \n — Случайное число - /roll &#127922; \n"))
    except Exception as e:
       print(repr(e))