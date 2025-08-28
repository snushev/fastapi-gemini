
import os
import time
from collections import defaultdict
from dotenv import load_dotenv
from fastapi import HTTPException, status


load_dotenv()

user_requests = defaultdict(list)

def apply_rate_limit(user_id: str):
    current_time = time.time()

    if user_id == "global_unauthenticated_user":
        rate_limit = int(os.getenv("GLOBAL_RATE_LIMIT"))
        time_window = int(os.getenv("GLOBAL_TIME_WINDOW_SECONDS"))
    else:
        rate_limit = int(os.getenv("AUTH_RATE_LIMIT"))
        time_window = int(os.getenv("AUTH_TIME_WINDOW_SECONDS"))

    user_requests[user_id] = [
        t for t in user_requests[user_id] if t > current_time - time_window
    ]

    if len(user_requests[user_id]) >= rate_limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Too many requests. Please try again later.",
        )
    else:
        current_usage = len(user_requests[user_id])
        print(f"User {user_id}: {current_usage + 1}/{rate_limit} requests used.")

    user_requests[user_id].append(current_time)
    return True