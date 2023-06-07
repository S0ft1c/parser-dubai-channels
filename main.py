from telethon import events
from database import db
from channel_handler import channel_handler
from create_client import client
from create_client import main_channel


help_text = """**Вот все команды:**

/add_channel <сам канал> - добавить новый канал на прослушку

/del_channel <сам канал> - удалить канал на прослушку

/list_channels - список всех каналов, которые на прослушке

/add_phrase <сама фраза> - добавить новую фразу (ключевое слово)

/del_phrase <сама фраза> - удалить фразу (ключевое слово)

/list_phrases - список всех фраз (ключевых слов)
"""

for c in [str(el[1]) for el in db.fetchall("SELECT * FROM channels")]:
    client.add_event_handler(channel_handler, events.NewMessage(c))


@client.on(events.NewMessage(main_channel)
async def main_channel_handler(event: events.NewMessage):
    print(event.media)
    print(db.fetchall("select * from channels"))
    print(db.fetchall("select * from phrases"))

    message = event.message.message

    # add new channel to database
    if message.startswith("/add_channel"):
        db.execute("INSERT INTO channels (channel) VALUES (?)",
                   (message.split()[1],))
        await client.send_message(event.chat_id, "Успешно доабвлен новый канал на прослушку!")
        client.add_event_handler(
            channel_handler, events.NewMessage(message.split()[1]))
        print(client.list_event_handlers())

    # delete channel from database
    elif message.startswith("/del_channel"):
        db.execute("DELETE FROM channels WHERE channel = ?",
                   (message.split()[1],))
        await client.send_message(event.chat_id, "Успешно удален канал на прослушку!")
        client.remove_event_handler(
            channel_handler, events.NewMessage(message.split()[1]))

    # list channels from database
    elif message.startswith("/list_channels"):
        ch = '\n'.join([str(el[1])
                       for el in db.fetchall("SELECT * FROM channels")])
        await client.send_message(event.chat_id, f"Список каналов на прослушку\n{ch}")

    # add new phrase to database
    elif message.startswith("/add_phrase"):
        db.execute("INSERT INTO phrases (phrase) VALUES (?)",
                   (message.split()[1],))
        await client.send_message(event.chat_id, "Успешно доабвлена новая плюс-фраза!")

    # delete phrase from database
    elif message.startswith("/del_phrase"):
        db.execute("DELETE FROM phrases WHERE phrase = ?",
                   (message.split()[1],))
        await client.send_message(event.chat_id, "Успешно удалена плюс-фраза!")

    # list phrases from database
    elif message.startswith("/list_phrases"):
        ph = '\n'.join([str(el[1])
                       for el in db.fetchall("SELECT * FROM phrases")])
        await client.send_message(event.chat_id, f"Список плюс-фраз\n{ph}")

    elif message.startswith("/help"):
        await client.send_message(event.chat_id, help_text)


client.run_until_disconnected()
