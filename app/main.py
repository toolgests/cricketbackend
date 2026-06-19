# # # from fastapi import FastAPI
# # # from app.api.cricket_routes import router
# # # from app.scheduler import start_scheduler
# # # from app.api.cricket_routes import router as youtube_router

# # # app = FastAPI(title="Cricket Backend API")

# # # app.include_router(router)

# # # @app.on_event("startup")
# # # async def startup():
# # #     start_scheduler()

# # # @app.get("/")
# # # def health():
# # #     return {"status": "Backend running"}

# # # app = FastAPI()
# # # app.include_router(youtube_router)
# # from fastapi import FastAPI
# # from app.api.cricket_routes import router
# # from app.scheduler import start_scheduler
# # from app.scheduler import start_scheduler1
# # from app.scheduler import start_scheduler3
# # from app.services.all_matches_service import fetch_all_series


# # # from app.scheduler import start_scheduler2

# # app = FastAPI(title="Cricket Backend API")

# # # Include router ONCE
# # app.include_router(router)

# # @app.on_event("startup")
# # async def startup():
# #     start_scheduler()
# #     start_scheduler1()
# #     start_scheduler3()
# #     await fetch_all_series()
# #     # start_scheduler2()

# # @app.get("/")
# # def health():
# #     return {"status": "Backend running"}



# # # from fastapi import FastAPI
# # # from app.api.cricket_routes import router
# # # from app.scheduler import start_scheduler3
# # # from app.services.all_matches_service import fetch_all_series

# # # app = FastAPI(title="Cricket Backend API")

# # # app.include_router(router)

# # # @app.on_event("startup")
# # # async def startup():
# # #     start_scheduler3()
# # #     await fetch_all_series()  # 🔥 immediate data load

# # # @app.get("/")
# # # def health():
# # #     return {"status": "Backend running"}
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.api.cricket_routes import router
# from app.scheduler import start_scheduler, start_scheduler1, start_scheduler3
# from app.services.all_matches_service import fetch_all_series

# # ✅ Create app ONLY ONCE
# app = FastAPI(title="Cricket Backend API")

# # ✅ Add CORS middleware (IMPORTANT for Flutter Web)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],      # allow all origins (for now)
#     allow_credentials=True,
#     allow_methods=["*"],      # GET, POST, PUT, DELETE etc.
#     allow_headers=["*"],
# )

# # ✅ Include router
# app.include_router(router)

# # ✅ Startup events
# @app.on_event("startup")
# async def startup():
#     start_scheduler()
#     start_scheduler1()
#     start_scheduler3()
#     await fetch_all_series()

# # ✅ Health check
# @app.get("/")
# def health():
#     return {"status": "Backend running"}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.cricket_routes import router
from app.scheduler import start_scheduler

app = FastAPI(title="Cricket Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.on_event("startup")
async def startup():
    start_scheduler()


@app.get("/")
def health():
    return {"status": "Backend running"}