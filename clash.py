import requests
# from BRoK8 import Crrazy_8
import telebot

headers = {
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.clashofstats.com/',
    'DNT': '1',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

def Clash(idd):
    params = {
        'q': idd,
        'page': '0',
        'nameEquality': 'false',
    }
    response = requests.get('https://api.clashofstats.com/search/players', params=params, headers=headers).json()
    
    name = response['items'][0]['name']
    id = response['items'][0]['tag']
    expLevel = response['items'][0]['expLevel']
    clanName = response['items'][0]['clanName']
    town = response['items'][0]['townHallLevel']
    war = response['items'][0]['warStars']
    
    text = f"Name : {name} .\niD : {id} .\nName Tribe : {clanName} .\nLevel Account : {expLevel} .\nLevel Townhall : {town} .\nWarstars : {war} ."
    
    return text
    
token = "6407297105:AAFqbcqbklGpXdfZ-c3moC6nArs4w1c1Fu8"
bot = telebot.TeleBot(token,num_threads=30,skip_pending=True)

@bot.message_handler(commands=["start"])
def Welcome(message):
	bot.reply_to(message,f'''اهلا بك عزيزي {message.from_user.first_name}

في بوت إظهار  المعلومات حساب كلاش اوف كلانس ، ارسل ايدي حسابك''',reply_markup=telebot.types.InlineKeyboardMarkup([
                     [telebot.types.InlineKeyboardButton(text='مبرمجي',url='tg://user?id=1315011160')]
                 ]))
                 
@bot.message_handler(content_types=['text'])
def innfo(message):
    idd = message.text
    idd = idd.replace('#','')
    try:
    	info = Clash(idd)
    	bot.reply_to(message,info)
    except:
    	bot.reply_to(message,'تأكد من الايدي عزيزي')
    
    #مبرمج الملف & @BRoK8
#قناتي & @Crrazy_8
bot.infinity_polling()