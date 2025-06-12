import os
import aiohttp

TELEGRAM_TOKEN = os.getenv("TG_TOKEN")
TELEGRAM_CHAT = os.getenv("TG_CHAT")
DISCORD_WEBHOOK = os.getenv("DISCORD_HOOK")

async def send_telegram(msg: str) -> None:
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    async with aiohttp.ClientSession() as session:
        await session.post(url, json={"chat_id": TELEGRAM_CHAT, "text": msg})

async def send_discord(msg: str) -> None:
    async with aiohttp.ClientSession() as session:
        await session.post(DISCORD_WEBHOOK, json={"content": msg})
