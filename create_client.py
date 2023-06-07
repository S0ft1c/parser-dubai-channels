from config import *
import telethon

api_id = id
api_hash = hash

client = telethon.TelegramClient(
    "read_client", api_id, api_hash, system_version="4.16.30-vxCUSTOM")
client.start()

