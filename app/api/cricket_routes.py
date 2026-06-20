from app.services.match_service import get_all_matches, get_ended_matches, get_live_matches
from fastapi import APIRouter
from app.cache import cache

router = APIRouter(prefix="/cricket", tags=["Cricket"])

# @router.get("/live")
# async def get_live_matches():
#     if cache["live_matches"]["data"] is None:
#         return {
#             "last_updated": None,
#             "matches": []
#         }

#     return {
#         "last_updated": cache["live_matches"]["last_updated"],
#         "matches": cache["live_matches"]["data"]
#     }

# @router.get("/live")
# async def get_live_matches():
#     live = cache.get("live_matches", {})

#     return {
#         "last_updated": live.get("last_updated"),
#         "matches": live.get("data") or []
#     }

# @router.get("/live")
# def live_matches():
#     return {
#         "last_updated": cache["last_updated"],
#         "matches": get_live_matches()
#     }

# @router.get("/ended")
# def ended_matches():
#     return {
#         "last_updated": cache["last_updated"],
#         "matches": get_ended_matches()
#     }

@router.get("/live")
def live_matches():
    return {
        "last_updated": (
            cache.get("last_updated").isoformat()
            if cache.get("last_updated")
            else None
        ),
        "matches": get_live_matches()
    }


@router.get("/ended")
def ended_matches():
    return {
        "last_updated": (
            cache.get("last_updated").isoformat()
            if cache.get("last_updated")
            else None
        ),
        "matches": get_ended_matches()
    }

@router.get("/all")
def all_matches():
    
    
    return {
        "last_updated": cache["last_updated"],
        "matches": get_all_matches()
    }


@router.get("/upcoming")
def get_upcoming_matches():
    return {
        "last_updated": cache["upcoming_matches"]["last_updated"],
        "matches": cache["upcoming_matches"]["data"]
    }

@router.get("/icc/highlights")
def icc_highlights_embed():
    return {
        "channel": "ICC",
        "type": "youtube_embed",
        "embed_url": "https://www.youtube.com/embed?listType=playlist&list=UUBZy7bU6CkXk9wYpF8KkXg"
    }
# @router.get("/all")
# async def get_all_matches():
#     data = cache.get("all_matches", {})

#     return {
#         "last_updated": data.get("last_updated"),
#         "matchType": [
#             "International",
#             "League",
#             "Domestic",
#             "Women"
#         ],
#         "data": data.get("data") or {}
#     }

@router.get("/series/all")
async def get_all_series():
    series = cache.get("all_series", {})

    return {
        "last_updated": series.get("last_updated"),
        "seriesType": [
            "International",
            "League",
            "Domestic",
            "Women"
        ],
        "data": series.get("data") or {}
    }
