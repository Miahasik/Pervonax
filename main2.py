import random
import random
from pyrogram import Client, filters
from loguru import logger


Client.channel_list: list = ["gkogtrgrtogtrpplg"]  # Список каналов
Client.text_list: list = ["Ефим хуй"]  # Список комментов

api_id = 18849118 # Сюда api_id полученный с https://my.telegram.org/apps
api_hash = "1a6a0c49a58ed513234295068dd94ad8"  # Сюда api_hash полученный с https://my.telegram.org/apps
app = Client("session", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.chat(Client.channel_list))
def comment_sender(Client, message):
    comment = Client.text_list[random.randint(0, len(Client.text_list) - 1)]
    post = Client.get_discussion_message(message.chat.id, message.id)
    post.reply(comment)
    logger.info(f"Оставил комментарий -> {comment}.")


if __name__ == '__main__':
    logger.info(f"Первонах запущен.")
    app.run()