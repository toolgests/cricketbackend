# import asyncio
# from app.services.cricket_fetcher import fetch_matches_from_api
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from app.services.cricket_service import fetch_live_matches
# from app.config import CACHE_REFRESH_INTERVAL
# from app.services.all_matches_service import fetch_all_series
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from app.services.upcoming_service import fetch_upcoming_matches
# # from app.services.all_matches_service import fetch_all_matches

# scheduler1 = AsyncIOScheduler()

# def start_scheduler1():
#     # fetch immediately
    
#     # asyncio.create_task(fetch_live_matches())
    
#     asyncio.create_task(fetch_matches_from_api())

#     # fetch every 20 seconds
#     scheduler1.add_job(
#         fetch_matches_from_api,
#         # fetch_live_matches,
#         "interval",
#         seconds=120
#     )

    
#     scheduler1.start()


# scheduler = AsyncIOScheduler()



# def start_scheduler():
#     # Run once immediately
    
#     asyncio.create_task(fetch_upcoming_matches())

#     # Then run every 3 hours
#     scheduler.add_job(
#         fetch_upcoming_matches,
#         "interval",
#         hours=10,
#         id="upcoming_interval",
#         replace_existing=True
#     )

#     scheduler.start()


# scheduler3 = AsyncIOScheduler()

# def start_scheduler3():
#     scheduler3.add_job(
#         fetch_all_series,
#         trigger="interval",
#         seconds=CACHE_REFRESH_INTERVAL,
#         id="all_series_job",
#         hours=24,
#         replace_existing=True,
#         max_instances=1
#     )

#     scheduler3.start()
#     print("✅ Scheduler started")



import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from app.services.cricket_fetcher import fetch_matches_from_api
from app.services.upcoming_service import fetch_upcoming_matches
from app.services.all_matches_service import fetch_all_series

# Single scheduler instance
scheduler = AsyncIOScheduler()


def start_scheduler():
    """
    Start all background jobs.
    """

    # Prevent starting twice
    if scheduler.running:
        print("✅ Scheduler already running")
        return

    # Run once immediately
    asyncio.create_task(fetch_matches_from_api())
    asyncio.create_task(fetch_upcoming_matches())
    asyncio.create_task(fetch_all_series())

    # Current matches every 2 minutes
    scheduler.add_job(
        fetch_matches_from_api,
        trigger="interval",
        seconds=120,
        id="matches_job",
        replace_existing=True,
        max_instances=1
    )

    # Upcoming matches every 10 hours
    scheduler.add_job(
        fetch_upcoming_matches,
        trigger="interval",
        hours=10,
        id="upcoming_job",
        replace_existing=True,
        max_instances=1
    )

    # All series every 24 hours
    scheduler.add_job(
        fetch_all_series,
        trigger="interval",
        hours=24,
        id="all_series_job",
        replace_existing=True,
        max_instances=1
    )

    scheduler.start()

    print("✅ Scheduler started successfully")