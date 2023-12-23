import nextcord
from nextcord.ext import commands
from pycoingecko import CoinGeckoAPI
import random
import schedule
import time
import asyncio
import config
cg = CoinGeckoAPI()


bot_bitcoin = commands.Bot()
bot_bnb = commands.Bot()
bot_doge = commands.Bot()
bot_eth = commands.Bot()
bot_ltc = commands.Bot()
bot_matic = commands.Bot()
bot_sol = commands.Bot()
bot_kaspa = commands.Bot()

bots = [bot_bitcoin, bot_bnb, bot_doge, bot_eth, bot_ltc, bot_matic, bot_sol, bot_kaspa]
coins = ["bitcoin","binancecoin","dogecoin","ethereum","litecoin","matic-network","solana","kaspa"]
info = cg.get_price(ids = coins, vs_currencies="usd", include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)


async def start(bot, coin, info=info):
    price = info[coin]["usd"]
    mcap = f'Market Cap: ${(round(int(info[coin]["usd_market_cap"]),0)):,}'
    vol = f'24h Vol: ${(round(int(info[coin]["usd_24h_vol"]),0)):,}'
    change = f'24h Change: {round(float(info[coin]["usd_24h_change"]),3)}%'
    
    try:
        if coin == 'kaspa':
            await bot.change_presence(activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = f'🍅{random.choice([mcap,vol,change])}'))
        else:
            await bot.change_presence(activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = f'{random.choice([mcap,vol,change])}'))
    except:
        pass
    if info[coin]["usd_24h_change"]<0:
        arrow = "(↘)"
    else:
        arrow = "(↗)"
    for guild in bot.guilds:
        try:
            await guild.get_member(int(bot.user.id)).edit(nick = f'{"$"}{price} {arrow}') 
        except nextcord.errors.Forbidden:
            pass
    

async def do():
    async def again():
        info = cg.get_price(ids = coins, vs_currencies="usd", include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)
        for count in range(len(bots)):
            await start(bots[count], coins[count],info)
    while True:
        await again()
        await asyncio.sleep(5*60)
        continue
    

#last bot only
@bot_kaspa.event
async def on_ready():
    await do()



loop = asyncio.get_event_loop()
loop.create_task(bot_bitcoin.start(config.bitcoin_token))
loop.create_task(bot_bnb.start(config.bnb_token))
loop.create_task(bot_doge.start(config.doge_token))
loop.create_task(bot_eth.start(config.eth_token))
loop.create_task(bot_ltc.start(config.ltc_token))
loop.create_task(bot_matic.start(config.matic_token))
loop.create_task(bot_sol.start(config.solana_token))
loop.create_task(bot_kaspa.run(config.kaspa_token))
loop.run_until_complete()

