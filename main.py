import nextcord
from nextcord.ext import commands
from pycoingecko import CoinGeckoAPI
import random
import schedule
import time
import asyncio
import config
cg = CoinGeckoAPI()


bot_algo= commands.Bot()
bot_ape =commands.Bot()
bot_atom = commands.Bot()
bot_avax = commands.Bot()
bot_banano = commands.Bot()
bot_bch = commands.Bot()
bot_bitcoin = commands.Bot()
bot_bnb = commands.Bot()
bot_cake = commands.Bot()
bot_cardano = commands.Bot()
bot_chainlink = commands.Bot()
bot_cronos  = commands.Bot()
bot_doge = commands.Bot()
bot_eos = commands.Bot()
bot_eth = commands.Bot()
bot_ltc = commands.Bot()
bot_mana = commands.Bot()
bot_matic = commands.Bot()
bot_monero = commands.Bot()
bot_polkadot = commands.Bot()
bot_sand = commands.Bot()
bot_sol = commands.Bot()
bot_tezos = commands.Bot()
bot_trx = commands.Bot()
bot_uniswap = commands.Bot()
bot_xlm = commands.Bot()
bot_xrp = commands.Bot()
bot_kaspa = commands.Bot()
bot_nano = commands.Bot()
bot_bat = commands.Bot()

bots = [bot_algo, bot_ape, bot_atom, bot_avax, bot_banano, bot_bch, bot_bitcoin, bot_bnb, bot_cake, bot_cardano, bot_chainlink, bot_cronos, bot_doge, bot_eos, bot_eth, bot_ltc,bot_mana, bot_matic, bot_monero, bot_polkadot, bot_sand, bot_sol,bot_tezos, bot_trx, bot_uniswap, bot_xlm, bot_xrp, bot_kaspa, bot_nano, bot_bat]
coins = ["algorand","apecoin","cosmos","avalanche-2","banano","bitcoin-cash","bitcoin","binancecoin", "pancakeswap-token","cardano","chainlink","crypto-com-chain","dogecoin","eos","ethereum","litecoin","decentraland","matic-network","monero","polkadot","the-sandbox","solana","tezos","tron","uniswap","stellar","ripple","kaspa", "nano", "basic-attention-token"]
info = cg.get_price(ids = coins, vs_currencies="usd", include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)


async def start(bot, coin):
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
    while True:
        info = cg.get_price(ids = coins, vs_currencies="usd", include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)
        for count in range(len(bots)):
            await start(bots[count],coins[count])
        await asyncio.sleep(3*60)
        continue
    

#last bot only
@bot_bat.event
async def on_ready():
    await do()



loop = asyncio.get_event_loop()
loop.create_task(bot_algo.start(config.algo_token))
loop.create_task(bot_ape.start(config.ape_token))
loop.create_task(bot_atom.start(config.atom_token))
loop.create_task(bot_avax.start(config.avax_token))
loop.create_task(bot_banano.start(config.banano_token))
loop.create_task(bot_bch.start(config.bch_token))
loop.create_task(bot_bitcoin.start(config.bitcoin_token))
loop.create_task(bot_bnb.start(config.bnb_token))
loop.create_task(bot_cake.start(config.cake_token))
loop.create_task(bot_cardano.start(config.cardano_token))
loop.create_task(bot_chainlink.start(config.chainlink_token))
loop.create_task(bot_cronos.start(config.cronos_token))
loop.create_task(bot_doge.start(config.doge_token))
loop.create_task(bot_eos.start(config.eos_token))
loop.create_task(bot_eth.start(config.eth_token))
loop.create_task(bot_ltc.start(config.ltc_token))
loop.create_task(bot_mana.start(config.mana_token))
loop.create_task(bot_matic.start(config.matic_token))
loop.create_task(bot_monero.start(config.monero_token))
loop.create_task(bot_polkadot.start(config.polkadot_token))
loop.create_task(bot_sand.start(config.sand_token))
loop.create_task(bot_sol.start(config.solana_token))
loop.create_task(bot_tezos.start(config.tezos_token))
loop.create_task(bot_trx.start(config.trx_token))
loop.create_task(bot_uniswap.start(config.uniswap_token))
loop.create_task(bot_xlm.start(config.xlm_token))
loop.create_task(bot_xrp.start(config.xrp_token))
loop.create_task(bot_kaspa.start(config.kaspa_token))
loop.create_task(bot_nano.start(config.nano_token))
loop.create_task(bot_bat.run(config.bat_token))
loop.run_until_complete()

