import os
import asyncio
import aiohttp
import websockets

HELIUS_KEY = os.getenv("HELIUS_KEY")
DEX_WS = "wss://io.dexscreener.com/ws"

async def fetch_solscan(address: str) -> dict:
    """Consulta datos de tokens en Solscan."""
    url = f"https://api.solscan.io/account/tokens?address={address}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()

async def dex_ws_listener(queue: asyncio.Queue) -> None:
    """Escucha pares nuevos mediante WebSocket de DexScreener."""
    async with websockets.connect(DEX_WS) as ws:
        await ws.send('{"type":"subscribe","topic":"pairs"}')
        async for msg in ws:
            await queue.put(msg)
