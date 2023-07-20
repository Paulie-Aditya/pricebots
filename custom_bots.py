import nextcord
from nextcord.ext import commands
import urllib.request 
import json
import asyncio
import random
import config

bot_rht = commands.Bot()
bot_pxa = commands.Bot()

rht_contract_address = "0xeaf363ae88e8d4083b5deb78eca37cd848c75b90"
pxa_contract_address = "0x1442c87f18fe2C770F779845802B13B509370b5e"



bots = [bot_rht, bot_pxa]
coins = ["rht", "pxa"]
addresses = {"rht": rht_contract_address, "pxa": pxa_contract_address}

async def start(bot, coin):
    api_url = f'https://api.dev.dex.guru/v1/chain/56/tokens/{addresses[coin]}/market/?api-key={config.dex_guru_api_key}'
    webUrl = urllib.request.urlopen(api_url)
    info = webUrl.read()
    info = str(info,'UTF-8')
    info.replace("'",'"')
    info_json = json.loads(info)

    price = (round(float(info_json['price_usd']),6))
    liq = f'Liquidity: ${round(float(info_json["liquidity_usd"]),2)}'
    vol = f'24h Vol: ${(round(float(info_json["volume_24h_usd"]),2)):,}'
    change = f'24h Change: {round(float(info_json["price_24h_delta_usd"]),3)}%'

    await bot.change_presence(activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = f'{random.choice([liq,vol,change])}'))

    if coin != 'pxa':
        if info_json["price_24h_delta_usd"]<0:
            arrow = "(↘)"
        else:
            arrow = "(↗)"
        for guild in bot.guilds:
            try:
                await guild.get_member(int(bot.user.id)).edit(nick = f'{"$"}{price} {arrow}') 
            except nextcord.errors.Forbidden:
                pass

    elif coin == 'pxa':
        xrp_contract_address = "0x1d2f0da169ceb9fc7b3144628db156f3f6c60dbe"
        xrp_api_url = f'https://api.dev.dex.guru/v1/chain/56/tokens/{xrp_contract_address}/market/?api-key={config.dex_guru_api_key}'
        xrp_webUrl = urllib.request.urlopen(xrp_api_url)
        xrp_info = xrp_webUrl.read()
        xrp_info = str(xrp_info,'UTF-8')
        xrp_info.replace("'",'"')
        xrp_json = json.loads(xrp_info)  
        xrp_price = xrp_json['price_usd']

        exchange_rate = round(float(price/xrp_price),3)

        nickname = f'${price} / {exchange_rate} XRP'

        for guild in bot.guilds:
            try:
                await guild.get_member(int(bot.user.id)).edit(nick = nickname) 
            except nextcord.errors.Forbidden:
                pass
    

async def do():
    async def again():
        for count in range(len(bots)):
            await start(bots[count], coins[count])
    while True:
        await asyncio.sleep(3*60)
        await again()
        continue



#last bot
@bot_pxa.event
async def on_ready():
    await do()

loop = asyncio.get_event_loop()
loop.create_task(bot_rht.start(config.rht_token))
loop.create_task(bot_pxa.run(config.pxa_token))
loop.run_until_complete()
