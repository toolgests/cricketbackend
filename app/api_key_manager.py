from datetime import datetime

ROTATION_HOURS = 3
START_TIME = datetime.utcnow()

def get_current_api_key(keys):
    elapsed_hours = int(
        (datetime.utcnow() - START_TIME).total_seconds() // 3600
    )
    index = (elapsed_hours // ROTATION_HOURS) % len(keys)
    return keys[index]
