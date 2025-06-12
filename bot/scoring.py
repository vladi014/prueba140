def compute_score(risk: dict, market: dict, social: dict, smart_money: dict) -> int:
    """Calcula la puntuación compuesta de un token."""
    seguridad = max(0, 50 - risk.get("penalizacion", 0))
    momentum = min(30, market.get("var_5m", 0) + market.get("var_1h", 0) + market.get("var_24h", 0))
    traccion = min(15, social.get("tweets_h", 0) + social.get("crec_telegram", 0))
    smart = 5 if smart_money.get("compras_pct", 0) >= 0.5 else 0
    return seguridad + momentum + traccion + smart
