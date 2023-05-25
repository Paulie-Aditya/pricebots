import { verifyKey, InteractionResponseType } from "discord-interactions";
import { Request, Router } from "itty-router";
import { getData, setNick } from "./utils.js";
import { CFRequest } from "@cloudflare/workers-types";
import { tickers } from "./tickers.js";

async function cronHandler(env) {
	const data = await getData([ ...tickers.keys() ], env.SCRAPER_API_KEY);

	for (let [ticker, displayName] of tickers.entries()) {
		const tokenVar = `TOKEN_${displayName.toUpperCase()}`;
		const token = env[tokenVar];
		if (!token) {
			console.warn(`You did not set a token for ${tokenVar}`);
			continue;
		}
		if (!data[ticker]) continue;
		await setNick(data[ticker], token);
	}
}

const router = Router();

router.get("/", _ => {
	return new Response("hi");
});
router.get("/cron", async (_, env) => {
	await cronHandler(env);

	return new Response("set nicks");
})
router.post("/interactions", _ => {
	return new Response(JSON.stringify({
      type: InteractionResponseType.PONG
    }), {
		headers: {
			"content-type": "application/json;charset=UTF-8",
		},
	});
});

export default {
  async fetch(request: CFRequest, env: any, event: any) {
    if (request.method === "POST") {
		const botName = new URL(request.url)?.searchParams?.get("bot") ?? "";
		const publicKey = env[`PUBLIC_KEY_${botName.toUpperCase()}`];
		console.log({ botName, publicKey });
		const signature = request.headers.get("x-signature-ed25519");
		const timestamp = request.headers.get("x-signature-timestamp");
		const body = await request.clone().arrayBuffer();
		const isValidRequest = botName && signature && timestamp && verifyKey(
			body,
			signature,
			timestamp,
			publicKey ?? ""
		);

		if (!isValidRequest) return new Response("Bad request signature.", { status: 401 });
	}

    return router.handle(request, env, event);
  },

  async scheduled(_: any, env: any, ctx: { waitUntil: (arg0: Promise<Response>) => any; }) {
    return ctx.waitUntil(cronHandler(env));
  }
};