# app/services/match_service.py

from app.cache import cache


def get_all_matches():
    """Return all matches from cache"""
    return cache.get("matches", [])


# def get_live_matches():
    """Return live matches"""
    matches = cache.get("matches", [])

    return [
        m for m in matches
        if m.get("matchStarted") is True
        and m.get("matchEnded") is False
    ]

def get_live_matches():
    matches = cache.get("matches", [])

    # print(type(matches))
    # print(matches[:1])

    return [
        m for m in matches
        if isinstance(m, dict)
        and m.get("matchStarted") is True
        and m.get("matchEnded") is False
    ]
def get_upcoming_matches():
    """Return upcoming matches"""

    matches = cache.get("matches", [])

    return [
        m for m in matches
        if m.get("matchStarted") is False
    ]


# def get_ended_matches():
#     """Return finished matches"""

#     matches = cache.get("matches", [])

#     return [
#         m for m in matches
#         if m.get("matchEnded") is True
#     ]


def get_ended_matches():
    matches = cache.get("matches", [])

    return [
        m for m in matches
        if isinstance(m, dict)
        and m.get("matchEnded") is True
    ]