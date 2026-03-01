import httpx
from datetime import datetime
from app.cache import cache
from app.config import RAPIDAPI_KEY, RAPIDAPI_HOST

UPCOMING_URL = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/upcoming"

async def fetch_upcoming_matches():
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": RAPIDAPI_HOST
    }

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.get(UPCOMING_URL, headers=headers)

            if response.status_code != 200:
                print("❌ RapidAPI error:", response.text)
                return

            data = response.json()

            cache["upcoming_matches"]["data"] = data
            cache["upcoming_matches"]["last_updated"] = datetime.utcnow()

            print("✅ Upcoming matches updated")

    except Exception as e:
        print("❌ Upcoming fetch failed:", str(e))
