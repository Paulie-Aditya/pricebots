import phin from "phin";

/**
 * Napkin.io function that fetches price data for tickers from coingecko
 * Coingecko blocks cloudflare workers from accessing their gateway for some reason :skull:
 */
export default async (req, res) => {
    const { tickers } = req.query || {};
    if (!tickers) return res.status(400).json({ error: "Malformed URL" });

    res.status(200).json((await phin({
        url: `https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true&precision=4&ids=${tickers}`,
        parse: "json"
    })).body);
};