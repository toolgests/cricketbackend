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


async def fetch_live_matches_completed():
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
                and match.get("matchEnded") is True
            ]

            # ✅ Sort matches by priority
            live_matches_sorted = sorted(
                live_matches,
                key=get_match_priority
            )

            live_matches_sorted = [
    normalize_scores(match)
    for match in live_matches_sorted
]

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


def normalize_scores(match):
    """
    Ensure score order follows teams order
    teams[0] score first
    teams[1] score second
    """

    teams = match.get("teams", [])
    scores = match.get("score", [])

    if not teams or not scores:
        return match

    team1 = teams[0].lower()
    team2 = teams[1].lower()

    team1_scores = []
    team2_scores = []

    for s in scores:
        inning = str(s.get("inning", "")).lower()

        if team1 in inning:
            team1_scores.append(s)

        elif team2 in inning:
            team2_scores.append(s)

    match["score"] = team1_scores + team2_scores
    return match
