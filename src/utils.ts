export function requestHandler(token: string) {
	return (endpoint: string, body?: object, method = "POST") => {
		const url = new URL(endpoint, "https://discord.com/api/v10/");
		const init = {
			method,
			headers: {
				Authorization: `Bot ${token}`,
				"Content-Type": "application/json"
			},
			body: body && JSON.stringify(body)
		};
		
		return fetch(url, init)
	};
};

const getDataUrl = new URL(`https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true&precision=4`);

type CoinData = {
	usd: number,
	usd_market_cap: number,
	usd_24h_vol: number,
	usd_24h_change: number,
	last_updated_at: number
};

export async function getData(tickers: string[], scraperApiKey: string) {
	getDataUrl.searchParams.append("ids", tickers.join(","));

	const scraperUrl = new URL("https://api.scraperapi.com");
	scraperUrl.searchParams.append("api_key", scraperApiKey);
	scraperUrl.searchParams.append("url", getDataUrl.href);
	const resp = await fetch(scraperUrl);

	if (resp.ok) return await resp.json() as { [key: string]: CoinData };
	throw new Error(await resp.text());
	return {};
}

export function getAllGuilds(token: string) {
	return requestHandler(token)("./users/@me/guilds", undefined, "GET").then(r => r.json());
}

// bot_info.update({bots[i]:{"Change":0,"Mcap":0,"Dailyvol":0,"Up_or_down":"","a1":"","a2":"","a3":"","Arrow":"","old_price":[0,0],"new_price":0}})

export async function setNick(data: CoinData, token: string) {
	const guilds = await getAllGuilds(token);
	const CHANGE_NICKNAME = (1n << 26n);

	for (const { id, permissions } of guilds) {
		if ((BigInt(permissions) & CHANGE_NICKNAME) !== (CHANGE_NICKNAME)) continue;

		await requestHandler(token)(`./guilds/${id}/members/@me`, {
			// f"{"$"}{bot_info[curr]["new_price"]}{" "}{bot_info[curr]["Arrow"]}")
			nick: `$${data.usd} (${data.usd_24h_change > 0 ? "↗" : "↘"})`
		}, "PATCH");
	}
}