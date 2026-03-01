import httpx
from datetime import datetime
from app.cache import cache
from app.config import RAPIDAPI_KEY, RAPIDAPI_HOST

SERIES_INTERNATIONAL_URL = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/International"
SERIES_LEAGUE_URL = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/League"
SERIES_DOMASTIC_URL = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/Domestic"
SERIES_WOMEN_URL = "https://cricbuzz-cricket.p.rapidapi.com/series/v1/Women"
MATCHES_UPCOMING_URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"

HEADERS = {
    "x-rapidapi-key": RAPIDAPI_KEY,
    "x-rapidapi-host": RAPIDAPI_HOST
}

async def fetch_all_series():
    try:
        async with httpx.AsyncClient(timeout=15) as client:
            intl_resp = await client.get(SERIES_INTERNATIONAL_URL, headers=HEADERS)
            leag_resp = await client.get(SERIES_LEAGUE_URL, headers=HEADERS)
            doms_resp = await client.get(SERIES_DOMASTIC_URL, headers=HEADERS)
            wome_resp = await client.get(SERIES_WOMEN_URL, headers=HEADERS)

            if intl_resp.status_code != 200:
                print("❌ Failed to fetch international series")
                return

            international = intl_resp.json()
            league = leag_resp.json()
            domestic= doms_resp.json()
            women = wome_resp.json()

            cache["all_series"]["data"] = {
                "International": international,
                "League": league,
                "Domestic": domestic,
                "Women": women
            }

            cache["all_series"]["last_updated"] = datetime.utcnow()
            print("✅ All series updated")

    except Exception as e:
        print("❌ Fetch all series failed:", str(e))
