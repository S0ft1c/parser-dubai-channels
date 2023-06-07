import telethon

api_id = input("API ID: ")
api_hash = input("API hash: ")
main_channel = input("Main channel: ")

client = telethon.TelegramClient(
    "read_client", api_id, api_hash, system_version="4.16.30-vxCUSTOM")
client.start()

