# app/services/cricket_fetcher.py

import httpx
from datetime import datetime
from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEYS
from app.cache import cache


async def fetch_matches_from_api():
    """
    Fetch matches from external cricket API
    and store them in cache.
    """

    url = f"{CRICKET_API_BASE_URL}/currentMatches"

    params = {
        "apikey":CRICKET_API_KEYS ,
        "offset": 0
    }

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.get(url, params=params)

            if response.status_code != 200:
                print("❌ HTTP Error:", response.status_code)
                return

            data = response.json()

            if data.get("status") != "success":
                print("❌ API Error:", data)
                return

            matches = data.get("data", [])

            # Store in cache
            cache["matches"] = matches
            cache["last_updated"] = datetime.utcnow()

            print(f"✅ Matches updated: {len(matches)}")

    except Exception as e:
        print("❌ Fetch error:", str(e))
