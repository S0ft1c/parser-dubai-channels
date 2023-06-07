from database import db
from telethon import events
from create_client import main_channel
from create_client import client


async def channel_handler(event: events.NewMessage):
    
    # receive all phrases from database
    ph = [str(el[1]) for el in db.fetchall("SELECT * FROM phrases")]
    message = event.message.message

    if "https://" in message or event.media is not None or message.__len__() > 200:  # check for anti-spamming
        pass
    else:
        for el in ph:
            if el in message.lower():
                print(event)
                # get the autor
                if event.message.post:  # if it's the post
                    author = f"**Это был пост из канала! Определить автора невозможно**"
                else:  # if it's the chat
                    author = await client.get_entity(event.message.from_id.user_id)
                    author = f"@{author.username}"
                
                # get the title of channel/chat
                title = await client.get_entity(event.message.peer_id.channel_id)
                title = title.username
                
                # this is the text of message
                text = f"""Сообщение поста: 💬
--- ---
{message}
--- ---
Пользователь 👤: {author}
--- ---
Ссылка на сообщение: https://t.me/{title}/{event.message.id}"""

                await event.client.send_message(main_channel, text)
                break
