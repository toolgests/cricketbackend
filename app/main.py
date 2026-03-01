# # from fastapi import FastAPI
# # from app.api.cricket_routes import router
# # from app.scheduler import start_scheduler
# # from app.api.cricket_routes import router as youtube_router

# # app = FastAPI(title="Cricket Backend API")

# # app.include_router(router)

# # @app.on_event("startup")
# # async def startup():
# #     start_scheduler()

# # @app.get("/")
# # def health():
# #     return {"status": "Backend running"}

# # app = FastAPI()
# # app.include_router(youtube_router)
# from fastapi import FastAPI
# import uvicorn
# from app.api.cricket_routes import router
# from app.scheduler import start_scheduler
# from app.scheduler import start_scheduler1
# from app.scheduler import start_scheduler3
# from app.services.all_matches_service import fetch_all_series


# # from app.scheduler import start_scheduler2

# app = FastAPI(title="Cricket Backend API")

# # Include router ONCE
# app.include_router(router)

# @app.on_event("startup")
# async def startup():
#     start_scheduler()
#     start_scheduler1()
#     start_scheduler3()
#     await fetch_all_series()
#     # start_scheduler2()

# @app.get("/")
# def health():
#     return {"status": "Backend running"}

# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         host="0.0.0.0",   # change host here
#         port=8000,
#         reload=True,
#         log_level="warning"
#     )

# # from fastapi import FastAPI
# # from app.api.cricket_routes import router
# # from app.scheduler import start_scheduler3
# # from app.services.all_matches_service import fetch_all_series

# # app = FastAPI(title="Cricket Backend API")

# # app.include_router(router)

# # @app.on_event("startup")
# # async def startup():
# #     start_scheduler3()
# #     await fetch_all_series()  # 🔥 immediate data load

# # @app.get("/")
# # def health():
# #     return {"status": "Backend running"}
import logging
from fastapi import FastAPI
import uvicorn

from app.api.cricket_routes import router
from app.scheduler import (
    start_scheduler,
    start_scheduler1,
    start_scheduler3,
)
from app.services.all_matches_service import fetch_all_series

# --------------------------------
# Logging config
# --------------------------------
logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s: %(message)s"
)

# --------------------------------
# FastAPI app
# --------------------------------
app = FastAPI(title="Cricket Backend API")
app.include_router(router)

# --------------------------------
# Startup event
# --------------------------------
@app.on_event("startup")
async def startup():
    start_scheduler()
    start_scheduler1()
    start_scheduler3()
    await fetch_all_series()

# --------------------------------
# Health check
# --------------------------------
@app.get("/")
def health():
    return {"status": "Backend running"}

# --------------------------------
# Run server (ADD THIS PART)
# --------------------------------
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",   # change host here
        port=8000,
        reload=True,
        log_level="warning"
    )
