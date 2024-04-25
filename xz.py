import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import events
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.messages import DeleteHistoryRequest, ReportSpamRequest
from telethon.tl.functions.contacts import BlockRequest

api_id = "22851446"
api_hash = "742f1f7aef2a98ff75bbf6e77bf590a5"

print(' Code Will Run .. Wait ')
print('  ')

SESSION = "1ApWapzMBu6J1tTN7V7wno1QJzsAxlj2Smp6DGWYrRFU341pOImn4cIsc0eBz7c4ARg4zXAaONrc0oTkiepC_skhnh9H39GkcDiTx0H-5GgHqbHckTm7BufCUvGlzAJYJkn-fd17-GkdBimlrEQYOBDj-CvPOGvdEaZRTEjf-bB4tsj8_rj_Mu-IAO8U6CnD9Kk73Lh71Vb7DSpQkqXFQyubezYxWQmb-hIeUCr0V5j0SPayJUpI_mW2rJDkUw-Upfir5tEscVbO47AV04xAKnP1XIOdFHTobiblWBy4dsr82IchxegULVma0sH3INhQNSZyFhCC91kMGti2035Tadv-pVxooCPs="

Hson = TelegramClient(StringSession(SESSION), api_id, api_hash)

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