from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from .database import get_db

app = FastAPI(title="MetaShift Analytics API")

# Crucial: This allows the local HTML/JS frontend to make requests to this backend without getting blocked by the browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/opportunities")
def get_opportunities(db: sqlite3.Connection = Depends(get_db)):
    """Developer Dashboard: Returns category metrics and opportunity scores."""
    cursor = db.cursor()
    # We query the analytical view built in the schema step
    cursor.execute("SELECT * FROM vw_category_opportunity ORDER BY opportunity_score DESC")
    return [dict(row) for row in cursor.fetchall()]

@app.get("/api/streams")
def get_live_streams(limit: int = 24, db: sqlite3.Connection = Depends(get_db)):
    """Streamer Dashboard: Returns the top live streams right now."""
    cursor = db.cursor()
    cursor.execute("""
        SELECT s.stream_title, s.viewer_count, s.thumbnail_url, s.stream_url,
               c.category_name, ch.broadcaster_name
        FROM live_snapshots s
        JOIN categories c ON s.category_id = c.category_id
        JOIN channels ch ON s.channel_id = ch.channel_id
        ORDER BY s.viewer_count DESC
        LIMIT ?
    """, (limit,))
    return [dict(row) for row in cursor.fetchall()]

@app.get("/api/suggestions")
def get_suggestions(db: sqlite3.Connection = Depends(get_db)):
    """Recommendation Engine: High opportunity score + proven audience."""
    cursor = db.cursor()
    cursor.execute("""
        SELECT category_name, total_viewers, active_streams, opportunity_score 
        FROM vw_category_opportunity
        WHERE total_viewers > 500 
        ORDER BY opportunity_score DESC
        LIMIT 6
    """)
    return [dict(row) for row in cursor.fetchall()]