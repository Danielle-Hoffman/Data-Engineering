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

def save_to_db(streams):
    """Inserts the stream data into the SQLite relational schema."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    inserted_count = 0
    
    for stream in streams:
        game_name = stream.get("game_name")
        
        # 1. The IRL Blocklist
        irl_categories = [
            "Just Chatting", "ASMR", "Art", "Music", "Sports", 
            "Special Events", "Talk Shows & Podcasts", "I'm Only Sleeping",
            "Pools, Hot Tubs, and Beaches", "Animals, Aquariums, and Zoos"
        ]
        
        # Skip if it's on the blocklist or has no category at all
        if game_name in irl_categories or not game_name:
            continue
            
        broadcaster = stream.get("user_name")
        title = stream.get("title")
        viewers = stream.get("viewer_count")
        
        # Twitch returns a template URL. We inject standard dimensions (320x180)
        thumbnail = stream.get("thumbnail_url").replace("{width}", "320").replace("{height}", "180")
        stream_url = f"https://twitch.tv/{broadcaster}"

        # 2. Ensure category exists and get its ID
        cursor.execute("INSERT OR IGNORE INTO categories (category_name) VALUES (?)", (game_name,))
        cursor.execute("SELECT category_id FROM categories WHERE category_name = ?", (game_name,))
        category_id = cursor.fetchone()[0]

        # 3. Ensure channel exists and get its ID
        cursor.execute("INSERT OR IGNORE INTO channels (broadcaster_name) VALUES (?)", (broadcaster,))
        cursor.execute("SELECT channel_id FROM channels WHERE broadcaster_name = ?", (broadcaster,))
        channel_id = cursor.fetchone()[0]

        # 4. Insert the live snapshot metric
        cursor.execute("""
            INSERT INTO live_snapshots (category_id, channel_id, stream_title, viewer_count, thumbnail_url, stream_url)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (category_id, channel_id, title, viewers, thumbnail, stream_url))
        
        inserted_count += 1

    conn.commit()
    conn.close()
    
    # Calculate how many were skipped to show in the terminal
    skipped = len(streams) - inserted_count
    print(f"✅ Successfully inserted {inserted_count} gaming streams (Filtered out {skipped} IRL streams).")
if __name__ == "__main__":
    print("Authenticating with Twitch...")
    token = get_twitch_token()
    
    print("Fetching live streams...")
    streams = fetch_live_streams(token)
    
    print("Saving to database...")
    save_to_db(streams)