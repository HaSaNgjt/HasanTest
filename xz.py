import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import events
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.messages import DeleteHistoryRequest, ReportSpamRequest
from telethon.tl.functions.contacts import BlockRequest

Hson.start()
async def is_contact(user_id):
    contacts = await Hson(GetContactsRequest(0))
    return any(user.id == user_id for user in contacts.users)

@Hson.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    if not await is_contact(sender.id):
        message_to_send = "زينب حالياً مموجودة واني مساعدها وميصير احد يراسلها"  # Customize the message here
        await event.respond(message_to_send)
        await asyncio.sleep(1)  # Wait 5 seconds before blocking

        await Hson(BlockRequest(sender.id))
        await asyncio.sleep(1)  # Wait 3 seconds before deleting history

        await Hson(DeleteHistoryRequest(peer=sender.id, max_id=0))
        await asyncio.sleep(2)  # Wait 2 seconds before reporting spam

        await Hson(ReportSpamRequest(sender.id))
        await Hson.send_message(
            'me',
            f"شلونج ي حلوة ❤️ \n"
            f"هذا الشخص راسلج وممكن يسببلك ازعاج ف حظرته وحذفته ع مودج يحلوة\n"
            f"وتدللين محد يضوجك دام اني موجود\n"
            f"يوزر الي مزعجك @{sender.username} I"
        )

Hson.start()
Hson.run_until_disconnected()