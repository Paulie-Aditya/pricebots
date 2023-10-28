# pricebots
Written in python by Paulie, being rewritten in javascript by [code913](https://code913.devpage.me) for [napkin.io](https://napkin.io) and [cloudflare workers](https://workers.cloudflare.com). Stuff may break because everything is being committed to the main branch.

Setup:
1. Create a napkin.io account (no credit card required).
1. Create a new napkin function
1. Paste everything from the file src/napkin/presence.js in this github repository into it.
1. Press the deploy button.
1. Go to the Other tab, scroll down and set bot tokens as environment variables for each of the currencies mentioned in the src/tickers.js file.
1. Create another function from the file src/napkin/coindata.js (you don't need to set bot tokens for this one) and deploy. **Remember the URLs of both the napkin functions**.
1. Install nodejs.
1. Create a cloudflare account (no credit card required).
1. Install wrangler with `npm i -g wrangler`.
1. Login to wrangler with `wrangler login`.
1. Clone this repository and `cd` into it.
1. Set the following environment variables using the `wrangler secret put VARIABLE_NAME` command:
    - The URL of the napkin functions you just deployed as `NAPKIN_PRESENCE_FUNCTION_URL` and `NAPKIN_COINDATA_FUNCTION_URL`
    - Discord bot tokens and their application public keys for each of the currencies mentioned in the src/tickers.js file.
1. Run `wrangler deploy`
1. Copy the returned deployment url (it should look like `pricebots.code913.workers.dev`)
1. Go to discord dev portal, and for each bot go to the interactions endpoint url input and set as `<the url>/interactions?bot=<capitalized display name>`  
  for example: to set bitcoin bot's url  
  ![screenshot of dev portal](./interactions.png)

Tokens should be in the format `TOKEN_CAPITALIZEDDISPLAYNAME` and public keys in the format `PUBLIC_KEY_CAPITALIZEDDISPLAYNAME`. the display name of the currency is the second value in the map  
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

PUBLIC_KEY_ALGO
PUBLIC_KEY_APE
PUBLIC_KEY_ATOM
PUBLIC_KEY_AVAX
```
