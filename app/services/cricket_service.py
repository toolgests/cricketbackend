# # # import httpx
# # # from datetime import datetime
# # # from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEY
# # # from app.cache import cache

# # # async def fetch_live_matches():
# # #     url = f"{CRICKET_API_BASE_URL}/currentMatches"

# # #     params = {
# # #         "apikey": CRICKET_API_KEY,
# # #         "offset": 0
# # #     }

# # #     async with httpx.AsyncClient(timeout=10) as client:
# # #         response = await client.get(url, params=params)
# # #         data = response.json()

# # #         # ❌ Do not cache invalid responses
# # #         if data.get("status") != "success":
# # #             print("Cricket API error:", data)
# # #             return

# # #         cache["live_matches"]["data"] = data["data"]
# # #         cache["live_matches"]["last_updated"] = datetime.utcnow()
# # import httpx
# # from datetime import datetime
# # from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEY
# # from app.cache import cache

# # async def fetch_live_matches():
# #     url = f"{CRICKET_API_BASE_URL}/currentMatches"

# #     params = {
# #         "apikey": CRICKET_API_KEY,
# #         "offset": 0
# #     }

# #     async with httpx.AsyncClient(timeout=10) as client:
# #         response = await client.get(url, params=params)
# #         data = response.json()

# #         # ❌ Do not cache invalid responses
# #         if data.get("status") != "success":
# #             print("Cricket API error:", data)
# #             return

# #         # ✅ FILTER ONLY LIVE MATCHES
# #         live_matches = [
# #             match for match in data.get("data", [])
# #             if match.get("matchStarted") is True
# #             and match.get("matchEnded") is False
# #         ]

# #         cache["live_matches"]["data"] = live_matches
# #         cache["live_matches"]["last_updated"] = datetime.utcnow()
# # # import httpx
# # # from datetime import datetime
# # # from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEY
# # # from app.cache import cache

# # # async def fetch_live_matches():
# # #     url = f"{CRICKET_API_BASE_URL}/currentMatches"
# # #     params = {
# # #         "apikey": CRICKET_API_KEY,
# # #         "offset": 0
# # #     }

# # #     try:
# # #         async with httpx.AsyncClient(timeout=10) as client:
# # #             response = await client.get(url, params=params)

# # #             # ✅ HTTP validation
# # #             if response.status_code != 200:
# # #                 print("HTTP error:", response.status_code)
# # #                 return

# # #             data = response.json()

# # #             # ✅ API validation
# # #             if data.get("status") != "success":
# # #                 print("Cricket API error:", data)
# # #                 return

# # #             # ✅ REAL-WORLD SAFE FILTER (works with all APIs)
# # #             live_matches = [
# # #                 match for match in data.get("data", [])
# # #                 if "live" in str(match.get("status", "")).lower()
# # #             ]

# # #             # ✅ Ensure cache exists
# # #             cache.setdefault("live_matches", {
# # #                 "data": [],
# # #                 "last_updated": None
# # #             })

# # #             cache["live_matches"]["data"] = live_matches
# # #             cache["live_matches"]["last_updated"] = datetime.utcnow()

# # #             print(f"Updated {len(live_matches)} live matches")

# # #     except Exception as e:
# # #         print("Live match fetch error:", str(e))

# import httpx
# from datetime import datetime
# from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEYS
# from app.cache import cache
# from app.api_key_manager import get_current_api_key

# async def fetch_live_matches():
#     url = f"{CRICKET_API_BASE_URL}/currentMatches"

#     api_key = get_current_api_key(CRICKET_API_KEYS)

#     params = {
#         "apikey": api_key,
#         "offset": 0
#     }

#     try:
#         async with httpx.AsyncClient(timeout=10) as client:
#             response = await client.get(url, params=params)
#             data = response.json()

#             # ❌ Invalid API response
#             if data.get("status") != "success":
#                 print("❌ Cricket API error:", data)
#                 return

#             # ✅ FILTER ONLY LIVE MATCHES
#             live_matches = [
#                 match for match in data.get("data", [])
#                 if match.get("matchStarted") is True
#                 and match.get("matchEnded") is False
#             ]

#             cache.setdefault("live_matches", {})
#             cache["live_matches"]["data"] = live_matches
#             cache["live_matches"]["last_updated"] = datetime.utcnow()

#             print(f"✅ Live matches updated using key: {api_key[-4:]}")

#     except Exception as e:
#         print("❌ Live match fetch failed:", str(e))
import httpx
from datetime import datetime
from app.config import CRICKET_API_BASE_URL, CRICKET_API_KEYS
from app.cache import cache
from app.api_key_manager import get_current_api_key


# 🏏 Priority keywords
INTERNATIONAL_KEYWORDS = [
    "india", "england", "australia", "pakistan", "new zealand",
    "south africa", "west indies", "bangladesh", "sri lanka",
    "icc", "world cup", "champions trophy", "asia cup"
]

DOMESTIC_KEYWORDS = [
    "ranji", "sheffield shield", "county", "vijay hazare",
    "syed mushtaq ali", "big bash", "ipl", "psl", "bpl", "cpl"
]


def get_match_priority(match):
    """
    Assign priority score to matches
    Lower number = Higher priority
    """

    name = str(match.get("name", "")).lower()

    # 1️⃣ International matches
    if any(keyword in name for keyword in INTERNATIONAL_KEYWORDS):
        return 1

    # 2️⃣ Domestic major tournaments
    if any(keyword in name for keyword in DOMESTIC_KEYWORDS):
        return 2

    # 3️⃣ Other matches
    return 3


async def fetch_live_matches():
    url = f"{CRICKET_API_BASE_URL}/currentMatches"

    api_key = get_current_api_key(CRICKET_API_KEYS)

    params = {
        "apikey": api_key,
        "offset": 0
    }

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url, params=params)

            if response.status_code != 200:
                print("❌ HTTP Error:", response.status_code)
                return

            data = response.json()

            # ❌ Invalid API response
            if data.get("status") != "success":
                print("❌ Cricket API error:", data)
                return

            # ✅ Filter only LIVE matches
            live_matches = [
                match for match in data.get("data", [])
                if match.get("matchStarted") is True
                and match.get("matchEnded") is False
            ]

            # ✅ Sort matches by priority
            live_matches_sorted = sorted(
                live_matches,
                key=get_match_priority
            )

            # ✅ Ensure cache exists
            cache.setdefault("live_matches", {
                "data": [],
                "last_updated": None
            })

            cache["live_matches"]["data"] = live_matches_sorted
            cache["live_matches"]["last_updated"] = datetime.utcnow()

            print(
                f"✅ Live matches updated ({len(live_matches_sorted)}) using key: {api_key[-4:]}"
            )

    except Exception as e:
        print("❌ Live match fetch failed:", str(e))
