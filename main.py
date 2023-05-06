import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import bot
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
import asyncio
import random

bot_algo= bot_ape= bot_atom= bot_avax= bot_banano= bot_bch = bot_bitcoin= bot_bnb= bot_cake= bot_cardano = bot_chainlink= bot_cronos = bot_dogecoin= bot_eos= bot_eth= discord.Bot()
bot_litecoin = bot_mana = bot_matic = bot_monero = bot_polkadot= bot_sand= bot_solana= bot_tezos= bot_trx= bot_uniswap= bot_xlm= bot_xrp = bot_nano = bot_bat = bot_kaspa = discord.Bot()


#pip install schedule
import schedule
import time

_status = {}


bots= ["Algo", "Ape", "Atom","Avax","Banano","Bch","Bitcoin","BNB","Cake","Cardano","Chainlink","Cronos","Dogecoin","Eos","Ethereum","Litecoin","Mana","Matic","Monero","Polkadot","Sand","Solana","Tezos","Trx","Uniswap","Xlm","Xrp","Nano","Kaspa","Bat"]
number_of_bots = len(bots)


bot_info = {}

for i in range(number_of_bots):
    bot_info.update({bots[i]:{"Change":0,"Mcap":0,"Dailyvol":0,"Up_or_down":"","a1":"","a2":"","a3":"","Arrow":"","old_price":[0,0],"new_price":0}})


changing_nick_in_time = 100

ids=["algorand","apecoin","cosmos","avalanche-2","banano","bitcoin-cash","bitcoin","binancecoin","pancakeswap-token","cardano","chainlink","crypto-com-chain","dogecoin","eos","ethereum","litecoin","decentraland","matic-network","monero","polkadot","the-sandbox","solana","tezos","tron","uniswap","stellar","ripple","kaspa", "nano", "basic-attention-token"]


def fetching_status():

    _status.update(cg.get_price(ids=ids, vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True))

    for j in range(number_of_bots):
        crypto= bot_info[bots[j]]
        crypto["Change"] = round(float(_status[ids[j]]["usd_24h_change"]),2)
        crypto["Mcap"] = f'{(round(int(_status[ids[j]]["usd_market_cap"]),0)):,}'
        crypto["Dailyvol"] = f'{(round(int(_status[ids[j]]["usd_24h_vol"]),0)):,}'

        if crypto["Change"] > 0:
            crypto["Up_or_down"] = "+"
        elif crypto["Change"] < 0:
            crypto["Up_or_down"] = "\u200b"

        if bots[j] == "Kaspa":
            bot_info[bots[j]["a1"]] = f'{"🍅 24h Change:"} {crypto["Up_or_down"]}{crypto["Change"]}{"%"}'
            bot_info[bots[j]["a2"]] = f'{"🍅 Market Cap: "}{"$"}{crypto["Mcap"]}'
            bot_info[bots[j]["a3"]] = f'{"🍅 24h Vol: "}{"$"}{crypto["Dailyvol"]}'
        else:
            bot_info[bots[j]["a1"]] = f'{"24h Change:"} {crypto["Up_or_down"]}{crypto["Change"]}{"%"}'
            bot_info[bots[j]["a2"]] = f'{"Market Cap: "}{"$"}{crypto["Mcap"]}'
            bot_info[bots[j]["a3"]] = f'{"24h Vol: "}{"$"}{crypto["Dailyvol"]}'



def start():
    y= cg.get_price(ids = ids, vs_currencies="usd")
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
                 await i.get_member(int(bot_algo.user.id)).edit(nick = f'{"$"}{bot_info["Algo"]["new_price"]}{" "}{bot_info["Algo"]["Arrow"]}')

             for i in bot_ape.guilds:
                 await i.get_member(int(bot_ape.user.id)).edit(nick = f'{"$"}{bot_info["Ape"]["new_price"]}{" "}{bot_info["Ape"]["Arrow"]}')

             for i in bot_atom.guilds:
                 await i.get_member(int(bot_atom.user.id)).edit(nick = f'{"$"}{bot_info["Atom"]["new_price"]}{" "}{bot_info["Atom"]["Arrow"]}')

             for i in bot_avax.guilds:
                 await i.get_member(int(bot_avax.user.id)).edit(nick = f'{"$"}{bot_info["Ape"]["Avax"]}{" "}{bot_info["Avax"]["Arrow"]}')

             for i in bot_banano.guilds:
                 await i.get_member(int(bot_banano.user.id)).edit(nick = f'{"$"}{bot_info["Banano"]["new_price"]}{" "}{bot_info["Banano"]["Arrow"]}')

             for i in bot_bch.guilds:
                 await i.get_member(int(bot_bch.user.id)).edit(nick = f'{"$"}{bot_info["Bch"]["new_price"]}{" "}{bot_info["Bch"]["Arrow"]}')

             for i in bot_bitcoin.guilds:
                 await i.get_member(int(bot_bitcoin.user.id)).edit(nick = f'{"$"}{bot_info["Bitcoin"]["new_price"]}{" "}{bot_info["Bitcoin"]["Arrow"]}')

             for i in bot_bnb.guilds:
                 await i.get_member(int(bot_bnb.user.id)).edit(nick = f'{"$"}{bot_info["BNB"]["new_price"]}{" "}{bot_info["BNB"]["Arrow"]}')

             for i in bot_cake.guilds:
                 await i.get_member(int(bot_cake.user.id)).edit(nick = f'{"$"}{bot_info["Cake"]["new_price"]}{" "}{bot_info["Cake"]["Arrow"]}')

             for i in bot_cardano.guilds:
                 await i.get_member(int(bot_cardano.user.id)).edit(nick = f'{"$"}{bot_info["Cardano"]["new_price"]}{" "}{bot_info["Cardano"]["Arrow"]}')

             for i in bot_chainlink.guilds:
                 await i.get_member(int(bot_chainlink.user.id)).edit(nick = f'{"$"}{bot_info["Chainlink"]["new_price"]}{" "}{bot_info["Chainlink"]["Arrow"]}')

             for i in bot_cronos.guilds:
                 await i.get_member(int(bot_cronos.user.id)).edit(nick = f'{"$"}{bot_info["Cronos"]["new_price"]}{" "}{bot_info["Cronos"]["Arrow"]}')

             for i in bot_dogecoin.guilds:
                 await i.get_member(int(bot_dogecoin.user.id)).edit(nick = f'{"$"}{bot_info["Dogecoin"]["new_price"]}{" "}{bot_info["Dogecoin"]["Arrow"]}')

             for i in bot_eos.guilds:
                 await i.get_member(int(bot_eos.user.id)).edit(nick = f'{"$"}{bot_info["Eos"]["new_price"]}{" "}{bot_info["Eos"]["Arrow"]}')

             for i in bot_eth.guilds:
                 await i.get_member(int(bot_eth.user.id)).edit(nick = f'{"$"}{bot_info["Ethereum"]["new_price"]}{" "}{bot_info["Ethereum"]["Arrow"]}')

             for i in bot_litecoin.guilds:
                 await i.get_member(int(bot_litecoin.user.id)).edit(nick = f'{"$"}{bot_info["Litecoin"]["new_price"]}{" "}{bot_info["Litecoin"]["Arrow"]}')

             for i in bot_mana.guilds:
                 await i.get_member(int(bot_mana.user.id)).edit(nick = f'{"$"}{bot_info["Mana"]["new_price"]}{" "}{bot_info["Mana"]["Arrow"]}')

             for i in bot_matic.guilds:
                 await i.get_member(int(bot_matic.user.id)).edit(nick = f'{"$"}{bot_info["Matic"]["new_price"]}{" "}{bot_info["Matic"]["Arrow"]}')

             for i in bot_monero.guilds:
                 await i.get_member(int(bot_monero.user.id)).edit(nick = f'{"$"}{bot_info["Monero"]["new_price"]}{" "}{bot_info["Monero"]["Arrow"]}')

             for i in bot_polkadot.guilds:
                 await i.get_member(int(bot_polkadot.user.id)).edit(nick = f'{"$"}{bot_info["Polkadot"]["new_price"]}{" "}{bot_info["Polkadot"]["Arrow"]}')

             for i in bot_sand.guilds:
                 await i.get_member(int(bot_sand.user.id)).edit(nick = f'{"$"}{bot_info["Sand"]["new_price"]}{" "}{bot_info["Sand"]["Arrow"]}')

             for i in bot_solana.guilds:
                 await i.get_member(int(bot_solana.user.id)).edit(nick = f'{"$"}{bot_info["Solana"]["new_price"]}{" "}{bot_info["Solana"]["Arrow"]}')

             for i in bot_tezos.guilds:
                 await i.get_member(int(bot_tezos.user.id)).edit(nick = f'{"$"}{bot_info["Tezos"]["new_price"]}{" "}{bot_info["Tezos"]["Arrow"]}')

             for i in bot_trx.guilds:
                 await i.get_member(int(bot_trx.user.id)).edit(nick = f'{"$"}{bot_info["Trx"]["new_price"]}{" "}{bot_info["Trx"]["Arrow"]}')

             for i in bot_uniswap.guilds:
                 await i.get_member(int(bot_uniswap.user.id)).edit(nick = f'{"$"}{bot_info["Uniswap"]["new_price"]}{" "}{bot_info["Uniswap"]["Arrow"]}')

             for i in bot_xlm.guilds:
                 await i.get_member(int(bot_xlm.user.id)).edit(nick = f'{"$"}{bot_info["Xlm"]["new_price"]}{" "}{bot_info["Xlm"]["Arrow"]}')

             for i in bot_xrp.guilds:
                 await i.get_member(int(bot_xrp.user.id)).edit(nick = f'{"$"}{bot_info["Xrp"]["new_price"]}{" "}{bot_info["Xrp"]["Arrow"]}')

             for i in bot_nano.guilds:
                 await i.get_member(int(bot_nano.user.id)).edit(nick = f'{"$"}{bot_info["Nano"]["new_price"]}{" "}{bot_info["Nano"]["Arrow"]}')

             for i in bot_kaspa.guilds:
                 await i.get_member(int(bot_kaspa.user.id)).edit(nick = f'{"$"}{bot_info["Kaspa"]["new_price"]}{" "}{bot_info["Kaspa"]["Arrow"]}')

             for i in bot_bat.guilds:
                 await i.get_member(int(bot_bat.user.id)).edit(nick = f'{"$"}{bot_info["Bat"]["new_price"]}{" "}{bot_info["Bat"]["Arrow"]}')

            #bot_info["Algo"]["a1"],bot_info["Algo"]["a2"],bot_info["Algo"]["a3"]

             await bot_algo.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_algo,a2_algo,a3_algo])}'))
             await bot_ape.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_ape,a2_ape,a3_ape])}'))
             await bot_atom.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_atom,a2_atom,a3_atom])}'))
             await bot_avax.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_avax,a2_avax,a3_avax])}'))
             await bot_banano.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_banano,a2_banano,a3_banano])}'))
             await bot_bch.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_bch,a2_bch,a3_bch])}'))
             await bot_bitcoin.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_bitcoin,a2_bitcoin,a3_bitcoin])}'))
             await bot_bnb.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_bnb,a2_bnb,a3_bnb])}'))
             await bot_cake.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_cake,a2_cake,a3_cake])}'))
             await bot_cardano.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_cardano,a2_cardano,a3_cardano])}'))
             await bot_chainlink.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_chainlink,a2_chainlink,a3_chainlink])}'))
             await bot_cronos.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_cronos,a2_cronos,a3_cronos])}'))
             await bot_dogecoin.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_dogecoin,a2_dogecoin,a3_dogecoin])}'))
             await bot_eos.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_eos,a2_eos,a3_eos])}'))
             await bot_eth.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_ethereum,a2_ethereum,a3_ethereum])}'))
             await bot_litecoin.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_litecoin,a2_litecoin,a3_litecoin])}'))
             await bot_mana.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_mana,a2_mana,a3_mana])}'))
             await bot_matic.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_matic,a2_matic,a3_matic])}'))
             await bot_monero.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_monero,a2_monero,a3_monero])}'))
             await bot_polkadot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_polkadot,a2_polkadot,a3_polkadot])}'))
             await bot_sand.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_sand,a2_sand,a3_sand])}'))
             #await bot_shiba.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_shiba,a2_shiba,a3_shiba])}'))
             await bot_solana.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_solana,a2_solana,a3_solana])}'))
             await bot_tezos.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_tezos,a2_tezos,a3_tezos])}'))
             await bot_trx.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_trx,a2_trx,a3_trx])}'))
             await bot_uniswap.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_uniswap,a2_uniswap,a3_uniswap])}'))
             await bot_xlm.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_xlm,a2_xlm,a3_xlm])}'))
             await bot_xrp.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_xrp,a2_xrp,a3_xrp])}'))
             await bot_nano.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_nano,a2_nano,a3_nano])}'))
             await bot_bat.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_bat,a2_bat,a3_bat])}'))
             await bot_kaspa.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name = f'{random.choice([a1_kaspa,a2_kaspa,a3_kaspa])}'))

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


@bot_shiba.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot_shiba))

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







