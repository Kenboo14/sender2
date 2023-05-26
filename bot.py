from pyrogram import Client, filters

api_id = 27486395
api_hash = 'af6f9c8666fca1f5da9b427904d8a015'
bot_token = '6071792533:AAEWhn6DTClCsDbNeFNgw6oopPlZ6LRWb04'

app = Client('my_bot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)
owner_id = [5721492036, 1935806583]

def send_image_with_caption(channel_id, image_path, text):
    try:
        # Mengunggah gambar
        media = app.send_photo(chat_id=channel_id, photo=image_path, caption=text)
        print('Gambar terkirim ke channel', channel_id)
        return media
    except Exception as e:
        print('Gagal mengirim gambar ke channel', channel_id)
        print(str(e))
        return None

def send_image_and_edit_caption_to_channels(channel_ids, text):
    image_path = 'IMG_20230525_043448_921.jpg'  # Ganti dengan path file gambar yang ingin Anda kirimkan
    for channel_id in channel_ids:
        send_image_with_caption(channel_id, image_path, text)

@app.on_message(filters.command(['ch1']))
def ch1_command(client, message):
    text = message.text
    channel_ids = [-1001809632005, -1001820086673]  # Ganti dengan channel ID yang sesuai
    image_path = 'IMG_20230525_043509_774.jpg'  # Ganti dengan path file gambar yang ingin Anda kirimkan
    
    for channel_id in channel_ids:
        media = send_image_with_caption(channel_id, image_path, text)
        if media:
            # Menghapus perintah /ch1 dari pengirim
            client.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)
            break

@app.on_message(filters.private & filters.user(owner_id))
def handle_message_owner(client, message):
    text = message.text
    channel_ids = [-1001985436252, -1001891595565]  # Ganti dengan channel ID yang sesuai

    for channel_id in channel_ids:
        send_image_and_edit_caption_to_channels(channel_ids, text)

# Handler untuk perintah /start
@app.on_message(filters.command(['start']))
def start_command(client, message):
    text = "Halo! Bot sedang aktif."
    client.send_message(chat_id=message.chat.id, text=text)

app.run()
