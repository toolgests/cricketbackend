# from typing import Dict
# from datetime import datetime

# cache = {
#     "live_matches": {
#         "data": None,
#         "last_updated": None
#     }
# }

# cache = {
#     "upcoming_matches": {
#         "data": None,
#         "last_updated": None
#     }
# }
# cache = {
#     "live_matches": {
#         "data": None,
#         "last_updated": None
#     },
#     "upcoming_matches": {
#         "data": None,
#         "last_updated": None
#     }
# }
# app/cache.py

cache = {
      "all_matches": {
        "data": {},
        "last_updated": None
    },

    "live_matches": {
        "data": [],
        "last_updated": None
    },
    "upcoming_matches": {
        "data": [],
        "last_updated": None
    },

     "all_series": {
        "data": {},
        "last_updated": None
    }
    
}
# cache = {
#     "all_series": {
#         "data": {},
#         "last_updated": None
#     }
# }