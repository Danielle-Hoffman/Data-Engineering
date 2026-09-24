-- SQLite Schema for Multi-Genre Stream Analytics

CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    genre_type TEXT NOT NULL DEFAULT 'Gaming'
);

CREATE TABLE channels (
    channel_id INTEGER PRIMARY KEY AUTOINCREMENT,
    broadcaster_name TEXT NOT NULL UNIQUE,
    platform TEXT NOT NULL DEFAULT 'Twitch'
);

CREATE TABLE live_snapshots (
    snapshot_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    channel_id INTEGER,
    stream_title TEXT,
    viewer_count INTEGER DEFAULT 0,
    thumbnail_url TEXT,
    stream_url TEXT,
    recorded_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(category_id) REFERENCES categories(category_id),
    FOREIGN KEY(channel_id) REFERENCES channels(channel_id)
);

-- Analytical view to calculate market opportunity per category
CREATE VIEW vw_category_opportunity AS
SELECT 
    c.category_name,
    c.genre_type,
    COUNT(s.snapshot_id) AS active_streams,
    SUM(s.viewer_count) AS total_viewers,
    ROUND(AVG(s.viewer_count), 2) AS opportunity_score
FROM categories c
JOIN live_snapshots s ON c.category_id = s.category_id
WHERE s.recorded_at >= datetime('now', '-1 hour')
GROUP BY c.category_name, c.genre_type;