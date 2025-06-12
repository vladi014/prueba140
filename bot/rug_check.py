import os
import aiohttp

RUGCHECK_API = os.getenv("RUGCHECK_API")

async def check_lp_locked(mint: str) -> bool:
    """Verifica porcentaje de LP bloqueado y liquidez inicial."""
    url = f"https://rugcheck.example.com/api/{mint}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
    return (
        data.get("lp_locked_pct") == 100
        and data.get("liquidity_usdc", 0) >= 50_000
    )

async def verify_authorities(mint_info: dict) -> bool:
    """Confirma que mint y freeze authority estén renunciadas."""
    return (
        mint_info.get("mint_authority") is None
        and mint_info.get("freeze_authority") is None
    )
