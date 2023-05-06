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

        bot_info[bots[j]["Change"]] = round(float(_status[ids[j]]["usd_24h_change"]),2)
        bot_info[bots[j]["Mcap"]] = f'{(round(int(_status[ids[j]]["usd_market_cap"]),0)):,}'
        bot_info[bots[j]["Dailyvol"]] = f'{(round(int(_status[ids[j]]["usd_24h_vol"]),0)):,}'
        if bot_info[bots[j]["Change"]]  > 0:
            bot_info[bots[j]["Up_or_down"]] = "+"
        elif bot_info[bots[j]["Change"]] < 0:
            bot_info[bots[j]["Up_or_down"]] = "\u200b"
        if bots[j] != "Kaspa":
            bot_info[bots[j]["a1"]] = f'{"24h Change:"} {bot_info[bots[j]["Up_or_down"]]}{bot_info[bots[j]["Change"]]}{"%"}'
            bot_info[bots[j]["a2"]] = f'{"Market Cap: "}{"$"}{bot_info[bots[j]["Mcap"]]}'
            bot_info[bots[j]["a3"]] = f'{"24h Vol: "}{"$"}{bot_info[bots[j]["Dailyvol"]]}'
        else:
            bot_info[bots[j]["a1"]] = f'{"🍅 24h Change:"} {bot_info[bots[j]["Up_or_down"]]}{bot_info[bots[j]["Change"]]}{"%"}'
            bot_info[bots[j]["a2"]] = f'{"🍅 Market Cap: "}{"$"}{bot_info[bots[j]["Mcap"]]}'
            bot_info[bots[j]["a3"]] = f'{"🍅 24h Vol: "}{"$"}{bot_info[bots[j]["Dailyvol"]]}'

def start():
    y= cg.get_price(ids = ids, vs_currencies="usd")



    new_price_algo = y["algorand"]["usd"]
    new_price_ape = y["apecoin"]["usd"]
    new_price_atom =y["cosmos"]["usd"]
    new_price_avax = y["avalanche-2"]["usd"]
    new_price_banano =y["banano"]["usd"]
    new_price_bch =y["bitcoin-cash"]["usd"]
    new_price_bitcoin =y["bitcoin"]["usd"]
    new_price_bnb =y["binancecoin"]["usd"]
    new_price_cake =y["pancakeswap-token"]["usd"]
    new_price_cardano =y["cardano"]["usd"]
    new_price_chainlink =y["chainlink"]["usd"]
    new_price_cronos =y["crypto-com-chain"]["usd"]
    new_price_dogecoin =y["dogecoin"]["usd"]
    new_price_eos =y["eos"]["usd"]
    new_price_ethereum =y["ethereum"]["usd"]
    new_price_litecoin =y["litecoin"]["usd"]
    new_price_mana =y["decentraland"]["usd"]
    new_price_matic =y["matic-network"]["usd"]
    new_price_monero =y["monero"]["usd"]
    new_price_polkadot =y["polkadot"]["usd"]
    new_price_sand =y["the-sandbox"]["usd"]
    #new_price_shiba =y["shiba-inu"]["usd"]
    new_price_solana =y["solana"]["usd"]
    new_price_tezos =y["tezos"]["usd"]
    new_price_trx =y["tron"]["usd"]
    new_price_uniswap =y["uniswap"]["usd"]
    new_price_xlm =y["stellar"]["usd"]
    new_price_xrp =y["ripple"]["usd"]
    new_price_kaspa = y["kaspa"]["usd"]
    new_price_nano = y["nano"]["usd"]
    new_price_bat = y["basic-attention-token"]["usd"]



    global old_price_algo, old_price_ape, old_price_atom, old_price_avax ,old_price_banano,old_price_bch,old_price_bitcoin,old_price_bnb,old_price_cake,old_price_cardano,old_price_chainlink,old_price_cronos,old_price_dogecoin,old_price_eos,old_price_ethereum,old_price_litecoin,old_price_mana,old_price_matic,old_price_monero,old_price_polkadot,old_price_sand,old_price_shiba,old_price_solana,old_price_tezos,old_price_trx,old_price_uniswap,old_price_xlm,old_price_xrp, old_price_kaspa,old_price_bat,_arrow_algo, _arrow_ape, _arrow_atom, _arrow_avax ,_arrow_banano,_arrow_bch,_arrow_bitcoin,_arrow_bnb,_arrow_cake,_arrow_cardano,_arrow_chainlink,_arrow_cronos,_arrow_dogecoin,_arrow_eos,_arrow_ethereum,_arrow_litecoin,_arrow_mana,_arrow_matic,_arrow_monero,_arrow_polkadot,_arrow_sand,_arrow_shiba,_arrow_solana,_arrow_tezos,_arrow_trx,_arrow_uniswap,_arrow_xlm,_arrow_xrp, _arrow_kaspa, _arrow_bat
    global old_price_nano , _arrow_nano

    if float(old_price_algo[-1]) < float(new_price_algo):
         _arrow_algo = "(↗)"
    if float(old_price_algo[-1]) > float(new_price_algo):
         _arrow_algo = "(↘)"
    if len(old_price_algo)>50:
        old_price_algo= [0]
    if float(old_price_ape[-1]) < float(new_price_ape):
         _arrow_ape = "(↗)"
    if float(old_price_ape[-1]) > float(new_price_ape):
         _arrow_ape = "(↘)"
    if len(old_price_ape)>50:
        old_price_ape= [0]
    if float(old_price_atom[-1]) < float(new_price_atom):
         _arrow_atom = "(↗)"
    if float(old_price_atom[-1]) > float(new_price_atom):
         _arrow_atom = "(↘)"
    if len(old_price_atom)>50:
        old_price_atom= [0]
    if float(old_price_avax[-1]) < float(new_price_avax):
         _arrow_avax = "(↗)"
    if float(old_price_avax[-1]) > float(new_price_avax):
         _arrow_avax = "(↘)"
    if len(old_price_avax)>50:
        old_price_avax= [0]
    if float(old_price_banano[-1]) < float(new_price_banano):
         _arrow_banano = "(↗)"
    if float(old_price_banano[-1]) > float(new_price_banano):
         _arrow_banano = "(↘)"
    if len(old_price_banano)>50:
        old_price_banano= [0]
    if float(old_price_bch[-1]) < float(new_price_bch):
         _arrow_bch = "(↗)"
    if float(old_price_bch[-1]) > float(new_price_bch):
         _arrow_bch = "(↘)"
    if len(old_price_bch)>50:
        old_price_bch= [0]
    if float(old_price_bitcoin[-1]) < float(new_price_bitcoin):
         _arrow_bitcoin = "(↗)"
    if float(old_price_bitcoin[-1]) > float(new_price_bitcoin):
         _arrow_bitcoin = "(↘)"
    if len(old_price_bitcoin)>50:
        old_price_bitcoin= [0]
    if float(old_price_bnb[-1]) < float(new_price_bnb):
         _arrow_bnb = "(↗)"
    if float(old_price_bnb[-1]) > float(new_price_bnb):
         _arrow_bnb = "(↘)"
    if len(old_price_bnb)>50:
        old_price_bnb= [0]
    if float(old_price_cake[-1]) < float(new_price_cake):
         _arrow_cake = "(↗)"
    if float(old_price_cake[-1]) > float(new_price_cake):
         _arrow_cake = "(↘)"
    if len(old_price_cake)>50:
        old_price_cake= [0]
    if float(old_price_cardano[-1]) < float(new_price_cardano):
         _arrow_cardano = "(↗)"
    if float(old_price_cardano[-1]) > float(new_price_cardano):
         _arrow_cardano = "(↘)"
    if len(old_price_cardano)>50:
        old_price_cardano= [0]
    if float(old_price_chainlink[-1]) < float(new_price_chainlink):
         _arrow_chainlink = "(↗)"
    if float(old_price_chainlink[-1]) > float(new_price_chainlink):
         _arrow_chainlink = "(↘)"
    if len(old_price_chainlink)>50:
        old_price_chainlink= [0]
    if float(old_price_cronos[-1]) < float(new_price_cronos):
         _arrow_cronos = "(↗)"
    if float(old_price_cronos[-1]) > float(new_price_cronos):
         _arrow_cronos = "(↘)"
    if len(old_price_cronos)>50:
        old_price_cronos= [0]
    if float(old_price_dogecoin[-1]) < float(new_price_dogecoin):
         _arrow_dogecoin = "(↗)"
    if float(old_price_dogecoin[-1]) > float(new_price_dogecoin):
         _arrow_dogecoin = "(↘)"
    if len(old_price_dogecoin)>50:
        old_price_dogecoin= [0]
    if float(old_price_eos[-1]) < float(new_price_eos):
         _arrow_eos = "(↗)"
    if float(old_price_eos[-1]) > float(new_price_eos):
         _arrow_eos = "(↘)"
    if len(old_price_eos)>50:
        old_price_eos= [0]
    if float(old_price_ethereum[-1]) < float(new_price_ethereum):
         _arrow_ethereum = "(↗)"
    if float(old_price_ethereum[-1]) > float(new_price_ethereum):
         _arrow_ethereum = "(↘)"
    if len(old_price_ethereum)>50:
        old_price_ethereum= [0]
    if float(old_price_litecoin[-1]) < float(new_price_litecoin):
         _arrow_litecoin = "(↗)"
    if float(old_price_litecoin[-1]) > float(new_price_litecoin):
         _arrow_litecoin = "(↘)"
    if len(old_price_litecoin)>50:
        old_price_litecoin= [0]
    if float(old_price_mana[-1]) < float(new_price_mana):
         _arrow_mana = "(↗)"
    if float(old_price_mana[-1]) > float(new_price_mana):
         _arrow_mana = "(↘)"
    if len(old_price_mana)>50:
        old_price_mana= [0]
    if float(old_price_matic[-1]) < float(new_price_matic):
         _arrow_matic = "(↗)"
    if float(old_price_matic[-1]) > float(new_price_matic):
         _arrow_matic = "(↘)"
    if len(old_price_matic)>50:
        old_price_matic= [0]
    if float(old_price_monero[-1]) < float(new_price_monero):
         _arrow_monero = "(↗)"
    if float(old_price_monero[-1]) > float(new_price_monero):
         _arrow_monero = "(↘)"
    if len(old_price_monero)>50:
        old_price_monero= [0]
    if float(old_price_polkadot[-1]) < float(new_price_polkadot):
         _arrow_polkadot = "(↗)"
    if float(old_price_polkadot[-1]) > float(new_price_polkadot):
         _arrow_polkadot = "(↘)"
    if len(old_price_polkadot)>50:
        old_price_polkadot= [0]
    if float(old_price_sand[-1]) < float(new_price_sand):
         _arrow_sand = "(↗)"
    if float(old_price_sand[-1]) > float(new_price_sand):
         _arrow_sand = "(↘)"
    if len(old_price_sand)>50:
        old_price_sand= [0]
    #if float(old_price_shiba[-1]) < float(new_price_shiba):
    #     _arrow_shiba = "(↗)"
    #if float(old_price_shiba[-1]) > float(new_price_shiba):
    #     _arrow_shiba = "(↘)"
    #if len(old_price_shiba)>50:
    #    old_price_shiba= [0]
    if float(old_price_solana[-1]) < float(new_price_solana):
         _arrow_solana = "(↗)"
    if float(old_price_solana[-1]) > float(new_price_solana):
         _arrow_solana = "(↘)"
    if len(old_price_solana)>50:
        old_price_solana= [0]
    if float(old_price_tezos[-1]) < float(new_price_tezos):
         _arrow_tezos = "(↗)"
    if float(old_price_tezos[-1]) > float(new_price_tezos):
         _arrow_tezos = "(↘)"
    if len(old_price_tezos)>50:
        old_price_tezos= [0]
    if float(old_price_trx[-1]) < float(new_price_trx):
         _arrow_trx = "(↗)"
    if float(old_price_trx[-1]) > float(new_price_trx):
         _arrow_trx = "(↘)"
    if len(old_price_trx)>50:
        old_price_trx= [0]
    if float(old_price_uniswap[-1]) < float(new_price_uniswap):
         _arrow_uniswap = "(↗)"
    if float(old_price_uniswap[-1]) > float(new_price_uniswap):
         _arrow_uniswap = "(↘)"
    if len(old_price_uniswap)>50:
        old_price_uniswap= [0]
    if float(old_price_xlm[-1]) < float(new_price_xlm):
         _arrow_xlm = "(↗)"
    if float(old_price_xlm[-1]) > float(new_price_xlm):
         _arrow_xlm = "(↘)"
    if len(old_price_xlm)>50:
        old_price_xlm= [0]
    if float(old_price_xrp[-1]) < float(new_price_xrp):
         _arrow_xrp = "(↗)"
    if float(old_price_xrp[-1]) > float(new_price_xrp):
         _arrow_xrp = "(↘)"
    if len(old_price_xrp)>50:
        old_price_xrp= [0]
    if float(old_price_kaspa[-1]) < float(new_price_kaspa):
         _arrow_kaspa = "(↗)"
    if float(old_price_kaspa[-1]) > float(new_price_kaspa):
         _arrow_kaspa = "(↘)"
    if len(old_price_kaspa)>50:
        old_price_kaspa= [0]
    if float(old_price_nano[-1]) < float(new_price_nano):
         _arrow_nano = "(↗)"
    if float(old_price_nano[-1]) > float(new_price_nano):
         _arrow_nano = "(↘)"
    if len(old_price_nano)>50:
        old_price_nano= [0]

    if float(old_price_bat[-1]) < float(new_price_bat):
         _arrow_bat = "(↗)"
    if float(old_price_bat[-1]) > float(new_price_bat):
         _arrow_bat = "(↘)"
    if len(old_price_bat)>50:
        old_price_bat= [0]


    old_price_algo.append(new_price_algo)
    old_price_ape.append(new_price_ape)
    old_price_atom.append(new_price_atom)
    old_price_avax.append(new_price_avax)
    old_price_banano.append(new_price_banano)
    old_price_bch.append(new_price_bch)
    old_price_bitcoin.append(new_price_bitcoin)
    old_price_bnb.append(new_price_bnb)
    old_price_cake.append(new_price_cake)
    old_price_cardano.append(new_price_cardano)
    old_price_chainlink.append(new_price_chainlink)
    old_price_cronos.append(new_price_cronos)
    old_price_dogecoin.append(new_price_dogecoin)
    old_price_eos.append(new_price_eos)
    old_price_ethereum.append(new_price_ethereum)
    old_price_litecoin.append(new_price_litecoin)
    old_price_mana.append(new_price_mana)
    old_price_matic.append(new_price_matic)
    old_price_monero.append(new_price_monero)
    old_price_polkadot.append(new_price_polkadot)
    old_price_sand.append(new_price_sand)
    #old_price_shiba.append(new_price_shiba)
    old_price_solana.append(new_price_solana)
    old_price_tezos.append(new_price_tezos)
    old_price_trx.append(new_price_trx)
    old_price_uniswap.append(new_price_uniswap)
    old_price_xlm.append(new_price_xlm)
    old_price_xrp.append(new_price_xrp)
    old_price_kaspa.append(new_price_kaspa)
    old_price_nano.append(new_price_nano)
    old_price_bat.append(new_price_bat)






async def all_changes():
    schedule.every().minute.do(fetching_status)
    schedule.every().minute.do(start)
    while True:
        try:
         global changing_nick_in_time, a1_algo, a1_ape, a1_atom, a1_avax , a1_banano, a1_bch, a1_bitcoin, a1_bnb, a1_cake,a1_cardano,a1_chainlink,a1_cronos,a1_dogecoin, a1_eos, a1_ethereum, a1_litecoin, a1_mana, a1_matic, a1_monero, a1_polkadot, a1_sand, a1_shiba, a1_solana, a1_tezos, a1_trx, a1_uniswap, a1_xlm, a1_xrp,a1_kaspa,a2_algo, a2_ape, a2_atom, a2_avax , a2_banano, a2_bch, a2_bitcoin, a2_bnb, a2_cake,a2_cardano,a2_chainlink,a2_cronos,a2_dogecoin, a2_eos, a2_ethereum, a2_litecoin, a2_mana, a2_matic, a2_monero, a2_polkadot, a2_sand, a2_shiba, a2_solana, a2_tezos, a2_trx, a2_uniswap, a2_xlm, a2_xrp ,a2_kaspa,a3_algo, a3_ape, a3_atom, a3_avax , a3_banano, a3_bch, a3_bitcoin, a3_bnb, a3_cake,a3_cardano,a3_chainlink,a3_cronos,a3_dogecoin, a3_eos, a3_ethereum, a3_litecoin, a3_mana, a3_matic, a3_monero, a3_polkadot, a3_sand, a3_shiba, a3_solana, a3_tezos, a3_trx, a3_uniswap, a3_xlm, a3_xrp, a3_kaspa
         global new_price_algo, new_price_ape, new_price_atom, new_price_avax ,new_price_banano,new_price_bch,new_price_bitcoin,new_price_bnb,new_price_cake,new_price_cardano,new_price_chainlink,new_price_cronos,new_price_dogecoin,new_price_eos,new_price_ethereum,new_price_litecoin,new_price_mana,new_price_matic,new_price_monero,new_price_polkadot,new_price_sand,new_price_shiba,new_price_solana,new_price_tezos,new_price_trx,new_price_uniswap,new_price_xlm,new_price_xrp, new_price_kaspa
         global  _arrow_algo, _arrow_ape, _arrow_atom, _arrow_avax ,_arrow_banano,_arrow_bch,_arrow_bitcoin,_arrow_bnb,_arrow_cake,_arrow_cardano,_arrow_chainlink,_arrow_cronos,_arrow_dogecoin,_arrow_eos,_arrow_ethereum,_arrow_litecoin,_arrow_mana,_arrow_matic,_arrow_monero,_arrow_polkadot,_arrow_sand,_arrow_shiba,_arrow_solana,_arrow_tezos,_arrow_trx,_arrow_uniswap,_arrow_xlm,_arrow_xrp, _arrow_kaspa
         global a1_nano, a2_nano, a3_nano, new_price_nano, _arrow_nano
         global a1_bat, a2_bat, a3_bat, new_price_bat, _arrow_bat
         changing_nick_in_time -=1
         if changing_nick_in_time == 0:
             for i in bot_algo.guilds:
                 await i.get_member(int(bot_algo.user.id)).edit(nick = f'{"$"}{new_price_algo}{" "}{_arrow_algo}')

             for i in bot_ape.guilds:
                 await i.get_member(int(bot_ape.user.id)).edit(nick = f'{"$"}{new_price_ape}{" "}{_arrow_ape}')


             for i in bot_atom.guilds:
                 await i.get_member(int(bot_atom.user.id)).edit(nick = f'{"$"}{new_price_atom}{" "}{_arrow_atom}')

             for i in bot_avax.guilds:
                 await i.get_member(int(bot_avax.user.id)).edit(nick = f'{"$"}{new_price_avax}{" "}{_arrow_avax}')

             for i in bot_banano.guilds:
                 await i.get_member(int(bot_banano.user.id)).edit(nick = f'{"$"}{new_price_banano}{" "}{_arrow_banano}')

             for i in bot_bch.guilds:
                 await i.get_member(int(bot_bch.user.id)).edit(nick = f'{"$"}{new_price_bch}{" "}{_arrow_bch}')

             for i in bot_bitcoin.guilds:
                 await i.get_member(int(bot_bitcoin.user.id)).edit(nick = f'{"$"}{new_price_bitcoin}{" "}{_arrow_bitcoin}')

             for i in bot_bnb.guilds:
                 await i.get_member(int(bot_bnb.user.id)).edit(nick = f'{"$"}{new_price_bnb}{" "}{_arrow_bnb}')

             for i in bot_cake.guilds:
                 await i.get_member(int(bot_cake.user.id)).edit(nick = f'{"$"}{new_price_cake}{" "}{_arrow_cake}')

             for i in bot_cardano.guilds:
                 await i.get_member(int(bot_cardano.user.id)).edit(nick = f'{"$"}{new_price_cardano}{" "}{_arrow_cardano}')

             for i in bot_chainlink.guilds:
                 await i.get_member(int(bot_chainlink.user.id)).edit(nick = f'{"$"}{new_price_chainlink}{" "}{_arrow_chainlink}')

             for i in bot_cronos.guilds:
                 await i.get_member(int(bot_cronos.user.id)).edit(nick = f'{"$"}{new_price_cronos}{" "}{_arrow_cronos}')

             for i in bot_dogecoin.guilds:
                 await i.get_member(int(bot_dogecoin.user.id)).edit(nick = f'{"$"}{new_price_dogecoin}{" "}{_arrow_dogecoin}')

             for i in bot_eos.guilds:
                 await i.get_member(int(bot_eos.user.id)).edit(nick = f'{"$"}{new_price_eos}{" "}{_arrow_eos}')

             for i in bot_eth.guilds:
                 await i.get_member(int(bot_eth.user.id)).edit(nick = f'{"$"}{new_price_ethereum}{" "}{_arrow_ethereum}')

             for i in bot_litecoin.guilds:
                 await i.get_member(int(bot_litecoin.user.id)).edit(nick = f'{"$"}{new_price_litecoin}{" "}{_arrow_litecoin}')

             for i in bot_mana.guilds:
                 await i.get_member(int(bot_mana.user.id)).edit(nick = f'{"$"}{new_price_mana}{" "}{_arrow_mana}')

             for i in bot_matic.guilds:
                 await i.get_member(int(bot_matic.user.id)).edit(nick = f'{"$"}{new_price_matic}{" "}{_arrow_matic}')

             for i in bot_monero.guilds:
                 await i.get_member(int(bot_monero.user.id)).edit(nick = f'{"$"}{new_price_monero}{" "}{_arrow_monero}')

             for i in bot_polkadot.guilds:
                 await i.get_member(int(bot_polkadot.user.id)).edit(nick = f'{"$"}{new_price_polkadot}{" "}{_arrow_polkadot}')

             for i in bot_sand.guilds:
                 await i.get_member(int(bot_sand.user.id)).edit(nick = f'{"$"}{new_price_sand}{" "}{_arrow_sand}')

             #for i in bot_shiba.guilds:
                # await i.get_member(int(bot_shiba.user.id)).edit(nick = f'{"$"}{new_price_shiba}{" "}{_arrow_shiba}')

             for i in bot_solana.guilds:
                 await i.get_member(int(bot_solana.user.id)).edit(nick = f'{"$"}{new_price_solana}{" "}{_arrow_solana}')

             for i in bot_tezos.guilds:
                 await i.get_member(int(bot_tezos.user.id)).edit(nick = f'{"$"}{new_price_tezos}{" "}{_arrow_tezos}')

             for i in bot_trx.guilds:
                 await i.get_member(int(bot_trx.user.id)).edit(nick = f'{"$"}{new_price_trx}{" "}{_arrow_trx}')

             for i in bot_uniswap.guilds:
                 await i.get_member(int(bot_uniswap.user.id)).edit(nick = f'{"$"}{new_price_uniswap}{" "}{_arrow_uniswap}')

             for i in bot_xlm.guilds:
                 await i.get_member(int(bot_xlm.user.id)).edit(nick = f'{"$"}{new_price_xlm}{" "}{_arrow_xlm}')

             for i in bot_xrp.guilds:
                 await i.get_member(int(bot_xrp.user.id)).edit(nick = f'{"$"}{new_price_xrp}{" "}{_arrow_xrp}')

             for i in bot_nano.guilds:
                 await i.get_member(int(bot_nano.user.id)).edit(nick = f'{"$"}{new_price_nano}{" "}{_arrow_nano}')

             for i in bot_kaspa.guilds:
                 await i.get_member(int(bot_kaspa.user.id)).edit(nick = f'{"$"}{new_price_kaspa}{" "}{_arrow_kaspa}')

             for i in bot_bat.guilds:
                 await i.get_member(int(bot_bat.user.id)).edit(nick = f'{"$"}{new_price_bat}{" "}{_arrow_bat}')


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







