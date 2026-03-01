# import httpx
# from datetime import datetime
# from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEY
# from app.cache import cache

# async def fetch_live_matches():
#     url = f"{CRICKET_API_BASE_URL}/currentMatches"

#     params = {
#         "apikey": CRICKET_API_KEY,
#         "offset": 0
#     }

#     async with httpx.AsyncClient(timeout=10) as client:
#         response = await client.get(url, params=params)
#         data = response.json()

#         # ❌ Do not cache invalid responses
#         if data.get("status") != "success":
#             print("Cricket API error:", data)
#             return

#         cache["live_matches"]["data"] = data["data"]
#         cache["live_matches"]["last_updated"] = datetime.utcnow()
import httpx
from datetime import datetime
from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEY
from app.cache import cache

async def fetch_live_matches():
    url = f"{CRICKET_API_BASE_URL}/currentMatches"

    params = {
        "apikey": CRICKET_API_KEY,
        "offset": 0
    }

    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url, params=params)
        data = response.json()

        # ❌ Do not cache invalid responses
        if data.get("status") != "success":
            print("Cricket API error:", data)
            return

        # ✅ FILTER ONLY LIVE MATCHES
        live_matches = [
            match for match in data.get("data", [])
            if match.get("matchStarted") is True
            and match.get("matchEnded") is False
        ]

        cache["live_matches"]["data"] = live_matches
        cache["live_matches"]["last_updated"] = datetime.utcnow()
# import httpx
# from datetime import datetime
# from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEY
# from app.cache import cache

# async def fetch_live_matches():
#     url = f"{CRICKET_API_BASE_URL}/currentMatches"
#     params = {
#         "apikey": CRICKET_API_KEY,
#         "offset": 0
#     }

#     try:
#         async with httpx.AsyncClient(timeout=10) as client:
#             response = await client.get(url, params=params)

#             # ✅ HTTP validation
#             if response.status_code != 200:
#                 print("HTTP error:", response.status_code)
#                 return

#             data = response.json()

#             # ✅ API validation
#             if data.get("status") != "success":
#                 print("Cricket API error:", data)
#                 return

#             # ✅ REAL-WORLD SAFE FILTER (works with all APIs)
#             live_matches = [
#                 match for match in data.get("data", [])
#                 if "live" in str(match.get("status", "")).lower()
#             ]

#             # ✅ Ensure cache exists
#             cache.setdefault("live_matches", {
#                 "data": [],
#                 "last_updated": None
#             })

#             cache["live_matches"]["data"] = live_matches
#             cache["live_matches"]["last_updated"] = datetime.utcnow()

#             print(f"Updated {len(live_matches)} live matches")

#     except Exception as e:
#         print("Live match fetch error:", str(e))
