import discord
import discord.ext
#from discord.ext import commands
#from discord.ext.commands import bot
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import asyncio
import random

import config

bot_algo= discord.Bot()
bot_ape= discord.Bot()
bot_atom= discord.Bot()
bot_avax= discord.Bot()
bot_banano= discord.Bot()
bot_bch = discord.Bot()
bot_bitcoin= discord.Bot()
bot_bnb= discord.Bot()
bot_cake= discord.Bot()
bot_cardano = discord.Bot()
bot_chainlink= discord.Bot()
bot_cronos = discord.Bot()
bot_dogecoin= discord.Bot()
bot_eos= discord.Bot()
bot_eth= discord.Bot()
bot_litecoin = discord.Bot()
bot_mana = discord.Bot()
bot_matic = discord.Bot()
bot_monero = discord.Bot()
bot_polkadot= discord.Bot()
bot_sand= discord.Bot()
bot_solana= discord.Bot()
bot_tezos= discord.Bot()
bot_trx= discord.Bot()
bot_uniswap= discord.Bot()
bot_xlm= discord.Bot()
bot_xrp = discord.Bot()
bot_nano = discord.Bot()
bot_bat = discord.Bot()
bot_kaspa = discord.Bot()


#pip install schedule
import schedule
import time

bots= ["Algo", "Ape", "Atom","Avax","Banano","Bch","Bitcoin","BNB","Cake","Cardano","Chainlink","Cronos","Dogecoin","Eos","Ethereum","Litecoin","Mana","Matic","Monero","Polkadot","Sand","Solana","Tezos","Trx","Uniswap","Xlm","Xrp","Nano","Kaspa","Bat"]
number_of_bots = len(bots)


bot_info = {}

for i in range(number_of_bots):
    bot_info.update({bots[i]:{"Change":0,"Mcap":0,"Dailyvol":0,"Up_or_down":"","a1":"","a2":"","a3":"","Arrow":"","old_price":[0,0],"new_price":0}})


changing_nick_in_time = 100

ids=["algorand","apecoin","cosmos","avalanche-2","banano","bitcoin-cash","bitcoin","binancecoin","pancakeswap-token","cardano","chainlink","crypto-com-chain","dogecoin","eos","ethereum","litecoin","decentraland","matic-network","monero","polkadot","the-sandbox","solana","tezos","tron","uniswap","stellar","ripple","kaspa", "nano", "basic-attention-token"]
#y = cg.get_price(ids=ids, vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True)

status = {}
def fetching_status():
    status.update(cg.get_price(ids=ids, vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True))
    for j in range(number_of_bots):
        crypto= bot_info[bots[j]]
        crypto["Change"] = round(float(status[ids[j]]["usd_24h_change"]),2)
        crypto["Mcap"] = f'{(round(int(status[ids[j]]["usd_market_cap"]),0)):,}'
        crypto["Dailyvol"] = f'{(round(int(status[ids[j]]["usd_24h_vol"]),0)):,}'

        if crypto["Change"] > 0:
            crypto["Up_or_down"] = "+"
        elif crypto["Change"] < 0:
            crypto["Up_or_down"] = "\u200b"

        if bots[j] == "Kaspa":
            bot_info["Kaspa"]["a1"] = f'{"🍅 24h Change:"} {crypto["Up_or_down"]}{crypto["Change"]}{"%"}'
            bot_info["Kaspa"]["a2"] = f'{"🍅 Market Cap: "}{"$"}{crypto["Mcap"]}'
            bot_info["Kaspa"]["a3"] = f'{"🍅 24h Vol: "}{"$"}{crypto["Dailyvol"]}'
        else:
            crypto["a1"] = f'{"24h Change:"} {crypto["Up_or_down"]}{crypto["Change"]}{"%"}'
            crypto["a2"] = f'{"Market Cap: "}{"$"}{crypto["Mcap"]}'
            crypto["a3"] = f'{"24h Vol: "}{"$"}{crypto["Dailyvol"]}'


def start():
    y = cg.get_price(ids=ids, vs_currencies='usd')
    for t in range(number_of_bots):
        crypto= bot_info[bots[t]]
        crypto["new_price"] = y[ids[t]]["usd"]

        if float(crypto["old_price"][-1]) < float(crypto["new_price"]):
            crypto["Arrow"] = "(↗)"
        elif float(crypto["old_price"][-1]) > float(crypto["new_price"]):
            _crypto["Arrow"] = "(↘)"
        if len(crypto["old_price"])>50:
            crypto["old_price"] = [0]

        (crypto["old_price"]).append(crypto["new_price"])



async def all_changes():
    schedule.every().minute.do(fetching_status)
    schedule.every().minute.do(start)
    while True:
        try:
         changing_nick_in_time -=1
         if changing_nick_in_time == 0:
             for i in bot_algo.guilds:
                 curr = "Algo"
                 await i.get_member(int(bot_algo.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_ape.guilds:
                 curr = "Ape"
                 await i.get_member(int(bot_ape.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_atom.guilds:
                 curr = "Atom"
                 await i.get_member(int(bot_atom.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_avax.guilds:
                 curr = "Avax"
                 await i.get_member(int(bot_avax.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_banano.guilds:
                 curr = "Banano"
                 await i.get_member(int(bot_banano.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_bch.guilds:
                 curr = "Bch"
                 await i.get_member(int(bot_bch.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_bitcoin.guilds:
                 curr = "Bitcoin"
                 await i.get_member(int(bot_bitcoin.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_bnb.guilds:
                 curr = "BNB"
                 await i.get_member(int(bot_bnb.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_cake.guilds:
                 curr = "Cake"
                 await i.get_member(int(bot_cake.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_cardano.guilds:
                 curr = "Cardano"
                 await i.get_member(int(bot_cardano.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_chainlink.guilds:
                 curr = "Chainlink"
                 await i.get_member(int(bot_chainlink.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_cronos.guilds:
                 curr = "Cronos"
                 await i.get_member(int(bot_cronos.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_dogecoin.guilds:
                 curr = "Dogecoin"
                 await i.get_member(int(bot_dogecoin.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_eos.guilds:
                 curr = "Eos"
                 await i.get_member(int(bot_eos.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_eth.guilds:
                 curr = "Ethereum"
                 await i.get_member(int(bot_eth.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_litecoin.guilds:
                 curr = "Litecoin"
                 await i.get_member(int(bot_litecoin.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_mana.guilds:
                 curr = "Mana"
                 await i.get_member(int(bot_mana.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_matic.guilds:
                 curr = "Matic"
                 await i.get_member(int(bot_matic.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_monero.guilds:
                 curr = "Monero"
                 await i.get_member(int(bot_monero.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_polkadot.guilds:
                 curr = "Polkadot"
                 await i.get_member(int(bot_polkadot.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_sand.guilds:
                 curr = "Sand"
                 await i.get_member(int(bot_sand.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_solana.guilds:
                 curr = "Solana"
                 await i.get_member(int(bot_solana.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_tezos.guilds:
                 curr = "Tezos"
                 await i.get_member(int(bot_tezos.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_trx.guilds:
                 curr = "Trx"
                 await i.get_member(int(bot_trx.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_uniswap.guilds:
                 curr = "Uniswap"
                 await i.get_member(int(bot_uniswap.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_xlm.guilds:
                 curr = "Xlm"
                 await i.get_member(int(bot_xlm.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_xrp.guilds:
                 curr = "Xrp"
                 await i.get_member(int(bot_xrp.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_nano.guilds:
                 curr = "Nano"
                 await i.get_member(int(bot_nano.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_kaspa.guilds:
                 curr = "Kaspa"
                 await i.get_member(int(bot_kaspa.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')

             for i in bot_bat.guilds:
                 curr = "Bat"
                 await i.get_member(int(bot_bat.user.id)).edit(nick = f'{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}')


             #choice = random.choice("a1","a2","a3")
             choice = "a1"
             await bot_algo.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name = f'{bot_info["Algo"][choice]}'))
             await bot_ape.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Ape"][choice]}'))
             await bot_atom.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Atom"][choice]}'))
             await bot_avax.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Avax"][choice]}'))
             await bot_banano.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Banano"][choice]}'))
             await bot_bch.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Bch"][choice]}'))
             await bot_bitcoin.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Bitcoin"][choice]}'))
             await bot_bnb.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["BNB"][choice]}'))
             await bot_cake.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Cake"][choice]}'))
             await bot_cardano.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Cardano"][choice]}'))
             await bot_chainlink.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Chainlink"][choice]}'))
             await bot_cronos.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Cronos"][choice]}'))
             await bot_dogecoin.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Dogecoin"][choice]}'))
             await bot_eos.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Eos"][choice]}'))
             await bot_eth.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Ethereum"][choice]}'))
             await bot_litecoin.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Litecoin"][choice]}'))
             await bot_mana.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Mana"][choice]}'))
             await bot_matic.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Matic"][choice]}'))
             await bot_monero.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Monero"][choice]}'))
             await bot_polkadot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Polkadot"][choice]}'))
             await bot_sand.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Sand"][choice]}'))
             await bot_solana.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Solana"][choice]}'))
             await bot_tezos.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Tezos"][choice]}'))
             await bot_trx.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Trx"][choice]}'))
             await bot_uniswap.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Uniswap"][choice]}'))
             await bot_xlm.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Xlm"][choice]}'))
             await bot_xrp.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Xrp"][choice]}'))
             await bot_nano.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Nano"][choice]}'))
             await bot_bat.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Bat"][choice]}'))
             await bot_kaspa.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{bot_info["Kaspa"][choice]}'))

             changing_nick_in_time +=100
             continue

        except:
            time.sleep(10)
            continue
        await asyncio.sleep(1)
        schedule.run_pending()







@bot_algo.event
async def on_ready():
    fetching_status()
    start()
    print('We have logged in as {0.user}'.format(bot_algo))

@bot_ape.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_ape))

@bot_atom.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_atom))

@bot_avax.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_avax))

@bot_banano.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_banano))

@bot_bch.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_bch))

@bot_bitcoin.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_bitcoin))

@bot_bnb.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_bnb))

@bot_cake.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_cake))

@bot_cardano.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_cardano))

@bot_chainlink.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_chainlink))

@bot_cronos.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_cronos))

@bot_dogecoin.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_dogecoin))

@bot_eos.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_eos))

@bot_eth.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_eth))

@bot_litecoin.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_litecoin))

@bot_mana.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_mana))

@bot_matic.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_matic))

@bot_monero.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_monero))


@bot_polkadot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_polkadot))

@bot_sand.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_sand))


@bot_solana.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_solana))

@bot_tezos.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_tezos))

@bot_trx.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_trx))

@bot_uniswap.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_uniswap))

@bot_xlm.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_xlm))

@bot_xrp.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_xrp))

@bot_nano.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_nano))

@bot_bat.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_bat))

@bot_kaspa.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_kaspa))
    await all_changes()

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
loop.create_task(bot_dogecoin.start(config.doge_token))
loop.create_task(bot_eos.start(config.eos_token))
loop.create_task(bot_eth.start(config.eth_token))
loop.create_task(bot_litecoin.start(config.ltc_token))
loop.create_task(bot_mana.start(config.mana_token))
loop.create_task(bot_matic.start(config.matic_token))
loop.create_task(bot_monero.start(config.monero_token))
loop.create_task(bot_polkadot.start(config.polkadot_token))
loop.create_task(bot_sand.start(config.sand_token))
loop.create_task(bot_solana.start(config.solana_token))
loop.create_task(bot_tezos.start(config.tezos_token))
loop.create_task(bot_trx.start(config.trx_token))
loop.create_task(bot_uniswap.start(config.uniswap_token))
loop.create_task(bot_xlm.start(config.xlm_token))
loop.create_task(bot_xrp.start(config.xrp_token))
loop.create_task(bot_nano.start(config.nano_token))
loop.create_task(bot_bat.start(config.bat_token))
loop.create_task(bot_kaspa.run(config.kaspa_token))
loop.run_until_complete()