# from fastapi import FastAPI
# from app.api.cricket_routes import router
# from app.scheduler import start_scheduler
# from app.api.cricket_routes import router as youtube_router

# app = FastAPI(title="Cricket Backend API")

# app.include_router(router)

# @app.on_event("startup")
# async def startup():
#     start_scheduler()

# @app.get("/")
# def health():
#     return {"status": "Backend running"}

# app = FastAPI()
# app.include_router(youtube_router)
from fastapi import FastAPI
from app.api.cricket_routes import router
from app.scheduler import start_scheduler
from app.scheduler import start_scheduler1
from app.scheduler import start_scheduler3
from app.services.all_matches_service import fetch_all_series


# from app.scheduler import start_scheduler2

app = FastAPI(title="Cricket Backend API")

# Include router ONCE
app.include_router(router)

@app.on_event("startup")
async def startup():
    start_scheduler()
    start_scheduler1()
    start_scheduler3()
    await fetch_all_series()
    # start_scheduler2()

@app.get("/")
def health():
    return {"status": "Backend running"}



# from fastapi import FastAPI
# from app.api.cricket_routes import router
# from app.scheduler import start_scheduler3
# from app.services.all_matches_service import fetch_all_series

# app = FastAPI(title="Cricket Backend API")

# app.include_router(router)

# @app.on_event("startup")
# async def startup():
#     start_scheduler3()
#     await fetch_all_series()  # 🔥 immediate data load

# @app.get("/")
# def health():
#     return {"status": "Backend running"}
