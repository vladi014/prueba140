# Bot de Análisis y Alerta de Memecoins en Solana

Este proyecto contiene el esqueleto de un bot escrito en **Python** que analiza memecoins en la red **Solana**. Integra datos on-chain, de mercado y sociales para calcular un *score* compuesto y detectar oportunidades o riesgos.

## Resumen ejecutivo
El bot filtra posibles *rug pulls* (liquidez bloqueada, autoridades renunciadas, distribución de holders) y combina información de diferentes APIs. Genera notificaciones por Telegram y Discord, almacenando datos en PostgreSQL y Redis. Todas las claves de API se leen desde variables de entorno.

## Diagrama de alto nivel
```
+-------------+      +-------------+      +-------------+
| data_feeds  | ---> | analysis    | ---> | scoring     |
| (on-chain,  |      | _engine     |      |             |
| mercado,    |      +-------------+      +-------------+
| social,     |              |                   |
| rugcheck)   |              v                   v
+-------------+      +-------------+      +-------------+
                           |                   |
                       +-------+          +---------+
                       | DB    |<---------| notifier|
                       +-------+          +---------+
                           ^
                           |
                    +--------------+
                    |  rug_check   |
                    +--------------+
```

## Módulos principales
- `data_feeds`: conexiones a WebSockets y APIs (Solscan, DexScreener, Birdeye).
- `rug_check`: validación de liquidez, autoridades y listas negras.
- `analysis_engine`: fusiona datos y aplica reglas de trading.
- `scoring`: calcula el *score* compuesto de cada token.
- `notifier`: envía alertas a Telegram y Discord.
- `main.py`: orquestación general con `asyncio`.

## Tabla de umbrales
| Parámetro                             | Valor por defecto | Variable |
|---------------------------------------|------------------|----------|
| LP bloqueado o quemado                | 100 %            | `MIN_LP_LOCK` |
| Liquidez inicial mínima             | 50 k USDC        | `MIN_LIQ_USDC` |
| Distribución Top 1 / Top 5           | <10 % / <25 %    | `MAX_TOP1`, `MAX_TOP5` |
| Supply quemado "verde"                | ≥30 %          | `MIN_BURN_PCT` |
| Volumen intra-hora para alerta        | >100 k USDC      | `ALERT_VOL_1H` |
| Incremento precio intra-hora          | ≥20 %          | `ALERT_PCT_15M` |
| Score mínimo para notificación       | ≥70           | `ALERT_SCORE` |

## Ejemplo de mensaje de alerta
```
🚨 Nuevo memecoin en tendencia: ABC
Score total: 74/100
• Seguridad: 45/50
• Momentum mercado: 20/30
• Tracción social: 9/15
• Smart-money: 0/5
Liquidez inicial 120k USDC, LP bloqueado 100 %
```

## Checklist diaria
1. Rotar claves de API (Helius, DexScreener, Twitter).
2. Verificar límites de llamadas y ajustar frecuencias.
3. Revisar logs en Loki para fallos de conexión.
4. Actualizar listas negras de RugCheck/SolSniffer.
5. Confirmar tamaño de PostgreSQL y Redis.
6. Reiniciar procesos si hay actualizaciones.
7. Probar bot de Telegram/Discord con un mensaje.

Este repositorio sirve como base para un bot completo de seguimiento de memecoins en Solana.
