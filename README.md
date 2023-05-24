# pricebots
written in python by Paulie, being rewritten in javascript by [code913](https://code913.devpage.me) for cloudflare workers.

you need to set the following environment variables using the `wrangler secret put VARIABLE_NAME` command:
1. an api key from [scraperapi.com](https://scraperapi.com)
1. 30 discord bot tokens for each of the currencies mentioned in the src/tickers.ts file. tokens should be in the format `TOKEN_CAPITALIZEDDISPLAYNAME`. the display name of the currency is the second value in the map  
for example:
```ts
["algorand", "Algo"],
["apecoin", "Ape"],
["cosmos", "Atom"],
["avalanche-2", "Avax"],
```
becomes
```
TOKEN_ALGO
TOKEN_APE
TOKEN_ATOM
TOKEN_AVAX
```