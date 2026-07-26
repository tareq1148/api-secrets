import os
import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("CLASS_TOKEN")

r = requests.get(
    "https://masar-class-api.a-f-almatrafi.workers.dev/api/secure/posts",
    headers={"Authorization": f"Bearer {token}"},
    timeout=10,
)
print(r.status_code)
