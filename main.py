from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


token = "Здесь должен быть токен вашего сообщества."
confs = ["Здесь", "должны", "быть", "перечислены", "все", "диалоги,", "в", "которые", "будут", "отправляться", "уведомления."]


def log(msg):
    print(f"\n\n{'=' * 10}\n{msg}\n{'=' * 10}\n")

def post(owner, id):
    vk.messages.send(message=f"На стене @{group['screen_name']} ({group['name']}) опубликована новая запись.", attachment=f'wall{owner}_{id}', peer_ids=",".join(confs), random_id=0)

print("Модули загружены, переменные объявлены. Авторизуюсь.")

for i in range(len(confs)): confs[i] = str(confs[i])

vk_session = VkApi(token=token)
vk = vk_session.get_api()
group = vk.groups.getById()[0]
gid = group["id"]
longpoll = VkBotLongPoll(vk_session, gid)

print("Авторизация успешна. Запуск цикла.")

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.WALL_POST_NEW:
                if event.object.post_type == "post":
                    log(f'Обнаружена новая запись на стене: wall{event.object["owner_id"]}_{event.object["id"]}')
                    post(event.object["owner_id"], event.object["id"])

    except Exception as e:
        log(f"Я упал((\nException: {e}")
