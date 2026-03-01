# import httpx
# from app.config import YOUTUBE_API_KEY, ICC_CHANNEL_ID

# YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"

# async def fetch_icc_latest_videos():
#     params = {
#         "part": "snippet",
#         "channelId": ICC_CHANNEL_ID,
#         "order": "date",
#         "maxResults": 10,
#         "type": "video",
#         "key": YOUTUBE_API_KEY
#     }

#     async with httpx.AsyncClient(timeout=10) as client:
#         res = await client.get(YOUTUBE_API_URL, params=params)
#         data = res.json()

#     videos = []
#     for item in data.get("items", []):
#         videos.append({
#             "video_id": item["id"]["videoId"],
#             "title": item["snippet"]["title"],
#             "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],
#             "published_at": item["snippet"]["publishedAt"]
#         })

#     return videos
import httpx
from app.config import YOUTUBE_API_KEY

ICC_UPLOADS_PLAYLIST_ID = "UUBZy7bU6CkXk9wYpF8KkXg"
YOUTUBE_PLAYLIST_API = "https://www.googleapis.com/youtube/v3/playlistItems"


async def fetch_icc_latest_videos():
    params = {
        "part": "snippet",
        "playlistId": ICC_UPLOADS_PLAYLIST_ID,
        "maxResults": 10,
        "key": YOUTUBE_API_KEY
    }

    async with httpx.AsyncClient(timeout=15) as client:
        response = await client.get(YOUTUBE_PLAYLIST_API, params=params)

    if response.status_code != 200:
        return {
            "channel": "ICC",
            "count": 0,
            "videos": [],
            "error": response.text
        }

    data = response.json()
    videos = []

    for item in data.get("items", []):
        snippet = item["snippet"]
        video_id = snippet["resourceId"]["videoId"]

        videos.append({
            "video_id": video_id,
            "title": snippet["title"],
            "thumbnail": snippet["thumbnails"]["high"]["url"],
            "published_at": snippet["publishedAt"]
        })

    return {
        "channel": "ICC",
        "count": len(videos),
        "videos": videos
    }
