## Database Diagram

```mermaid
erDiagram
    CATEGORIES {
        int category_id PK
        string category_name "e.g., Software Dev, Just Chatting"
        string genre_type "Gaming, Creative, Tech"
    }
    
    CHANNELS {
        int channel_id PK
        string broadcaster_name
        string platform "Default: Twitch"
    }
    
    LIVE_SNAPSHOTS {
        bigint snapshot_id PK
        int category_id FK
        int channel_id FK
        string stream_title
        int viewer_count
        string thumbnail_url
        string stream_url
        timestamp recorded_at
    }

    CATEGORIES ||--o{ LIVE_SNAPSHOTS : "groups"
    CHANNELS ||--o{ LIVE_SNAPSHOTS : "broadcasts"