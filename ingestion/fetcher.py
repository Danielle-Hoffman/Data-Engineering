import os 
import sqlite3
import requests 
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_APP_SECRET")
DB_PATH = "lobbystats.db"

def get_twitch_token():
    """Exchanges your Client ID and Secret for a temporary Access Token."""
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    response.raise_for_status()
    return response.json()["access_token"]

def fetch_live_streams(token):
    """Fetches the top 100 live streams currently on Twitch."""
    url = "https://api.twitch.tv/helix/streams"
    headers = {
        "Client-Id": CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }
    params = {"first": 100} 
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["data"]